import subprocess
import os
import sys

output_dir = "output"
video_file = os.path.join(output_dir, "final_video.mp4")
voice_file = os.path.join(output_dir, "voice.wav")

images = [
    "img_01.png",
    "img_02.png",
    "img_03.png",
    "img_04.png",
    "img_05.png",
]

# Safety checks
if not os.path.exists(voice_file):
    print("❌ voice.wav missing, cannot create video")
    sys.exit(1)

for img in images:
    if not os.path.exists(os.path.join(output_dir, img)):
        print(f"❌ Missing image: {img}")
        sys.exit(1)

# Create images.txt
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
    "-i", voice_file,
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-shortest",
    video_file
]

subprocess.run(command, check=True)

print("🎬 Video created successfully:", video_file)
