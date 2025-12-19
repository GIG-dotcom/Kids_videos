import subprocess
import os

output_dir = "output"
video_file = os.path.join(output_dir, "final_video.mp4")

images = [
    "img_01.png",
    "img_02.png",
    "img_03.png",
    "img_04.png",
    "img_05.png",
]

list_file = os.path.join(output_dir, "images.txt")
with open(list_file, "w") as f:
    for img in images:
        f.write(f"file '{img}'\n")
        f.write("duration 6\n")

command = [
    "ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", list_file,
    "-i", os.path.join(output_dir, "voice.wav"),
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-shortest",
    video_file
]

subprocess.run(command, check=True)

print("🎬 Video created:", video_file)
