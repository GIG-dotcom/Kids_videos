from moviepy import VideoFileClip, AudioFileClip, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

if not os.path.exists(AUDIO_FILE):
raise FileNotFoundError(f"Audio file missing: {AUDIO_FILE}")
# Paths
BACKGROUND_VIDEO = "assets/background.mp4"
AUDIO_FILE = "output/voice.wav"
OUTPUT_VIDEO = "output/final_video.mp4"

# Load audio
audio = AudioFileClip(AUDIO_FILE)
duration = audio.duration + 1  # little buffer

# Load & loop background video
bg = (
    VideoFileClip(BACKGROUND_VIDEO)
    .resize((720, 1280))
    .loop(duration=duration)
)

# Read story text
with open("output/story.txt") as f:
    story_text = f.read()

# ---------- CREATE TEXT IMAGE ----------
def create_text_image(text):
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 52)
    lines = textwrap.wrap(text, width=28)

    img = Image.new("RGBA", (680, len(lines) * 80 + 40), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    y = 20
    for line in lines:
        draw.text((20, y), line, font=font, fill="white")
        y += 70

    img_path = "output/text.png"
    img.save(img_path)
    return img_path

text_img = create_text_image(story_text)

text_clip = (
    ImageClip(text_img)
    .set_duration(duration)
    .set_position("center")
    .fadein(0.5)
    .fadeout(0.5)
)

# Combine video + text
final = CompositeVideoClip([bg, text_clip])
final = final.set_audio(audio)

# Export high quality
final.write_videofile(
    OUTPUT_VIDEO,
    fps=24,
    codec="libx264",
    audio_codec="aac",
    bitrate="4000k",
    threads=4
)

print("🎬 High-quality video created:", OUTPUT_VIDEO)
