from moviepy import (
    VideoFileClip,
    AudioFileClip,
    CompositeVideoClip,
    CompositeAudioClip,
    ImageClip,
)
from moviepy.audio.fx import audio_loop
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import sys

# -----------------------------
# PATHS (MATCH YOUR REPO)
# -----------------------------
BACKGROUND_VIDEO = "assets/background.mp4"
BACKGROUND_MUSIC = "Music/background_music.wav"
VOICE_AUDIO = "output/voice.wav"
STORY_FILE = "output/story.txt"

OUTPUT_VIDEO = "output/final_video.mp4"
TEXT_IMAGE = "output/text.png"

# -----------------------------
# SAFETY CHECKS
# -----------------------------
required_files = [
    BACKGROUND_VIDEO,
    BACKGROUND_MUSIC,
    VOICE_AUDIO,
    STORY_FILE,
]

for f in required_files:
    if not os.path.exists(f):
        print(f"❌ Required file missing: {f}")
        sys.exit(1)

os.makedirs("output", exist_ok=True)

# -----------------------------
# LOAD AUDIO
# -----------------------------
voice = AudioFileClip(VOICE_AUDIO)
music = AudioFileClip(BACKGROUND_MUSIC)

duration = max(30, voice.duration + 1)

music = audio_loop(music, duration=duration).with_volume_scaled(0.15)
voice = voice.with_volume_scaled(1.0)

final_audio = CompositeAudioClip([music, voice])

# -----------------------------
# LOAD BACKGROUND VIDEO
# -----------------------------
bg = (
    VideoFileClip(BACKGROUND_VIDEO)
    .resize((720, 1280))
    .loop(duration=duration)
)

# -----------------------------
# READ STORY TEXT
# -----------------------------
with open(STORY_FILE, "r") as f:
    story_text = f.read().strip()

if not story_text:
    print("❌ Story text is empty")
    sys.exit(1)

# -----------------------------
# CREATE TEXT IMAGE
# -----------------------------
def create_text_image(text):
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 52)
    lines = textwrap.wrap(text, width=28)

    img_height = len(lines) * 80 + 40
    img = Image.new("RGBA", (680, img_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    y = 20
    for line in lines:
        draw.text((20, y), line, font=font, fill="white")
        y += 70

    img.save(TEXT_IMAGE)
    return TEXT_IMAGE

text_image_path = create_text_image(story_text)

# -----------------------------
# TEXT CLIP
# -----------------------------
text_clip = (
    ImageClip(text_image_path)
    .set_duration(duration)
    .set_position("center")
    .fadein(0.5)
    .fadeout(0.5)
)

# -----------------------------
# COMPOSE FINAL VIDEO
# -----------------------------
final = CompositeVideoClip([bg, text_clip])
final = final.set_audio(final_audio)

# -----------------------------
# EXPORT VIDEO
# -----------------------------
final.write_videofile(
    OUTPUT_VIDEO,
    fps=24,
    codec="libx264",
    audio_codec="aac",
    bitrate="4500k",
    threads=4,
    preset="medium",
)

print("🎬 Video created successfully:", OUTPUT_VIDEO)
