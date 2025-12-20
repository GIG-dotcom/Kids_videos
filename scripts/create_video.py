from moviepy import (
    VideoFileClip,
    AudioFileClip,
    CompositeVideoClip,
    CompositeAudioClip,
    ImageClip,
)
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import sys

# -----------------------------
# PATHS
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
for f in [BACKGROUND_VIDEO, BACKGROUND_MUSIC, VOICE_AUDIO, STORY_FILE]:
    if not os.path.exists(f):
        print(f"❌ Missing file: {f}")
        sys.exit(1)

os.makedirs("output", exist_ok=True)

# -----------------------------
# LOAD AUDIO (MoviePy 2.2.x)
# -----------------------------
voice = AudioFileClip(VOICE_AUDIO)
music = AudioFileClip(BACKGROUND_MUSIC)

duration = max(30, voice.duration + 1)

if music.duration >= duration:
    music = music.subclipped(0, duration)
else:
    repeats = int(duration // music.duration) + 1
    music = CompositeAudioClip([music] * repeats).subclipped(0, duration)

music = music.with_volume_scaled(0.15)
voice = voice.with_volume_scaled(1.0)

final_audio = CompositeAudioClip([music, voice])

# -----------------------------
# LOAD BACKGROUND VIDEO
# -----------------------------
bg = (
    VideoFileClip(BACKGROUND_VIDEO)
    .resized((720, 1280))
    .looped(duration=duration)
)

# -----------------------------
# READ STORY
# -----------------------------
with open(STORY_FILE, "r") as f:
    story_text = f.read().strip()

if not story_text:
    print("❌ Story text empty")
    sys.exit(1)

# -----------------------------
# CREATE TEXT IMAGE
# -----------------------------
def create_text_image(text):
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 52)
    lines = textwrap.wrap(text, width=28)

    img = Image.new("RGBA", (680, len(lines) * 80 + 40), (0, 0, 0, 0))
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
    .with_duration(duration)
    .with_position("center")
    .with_fadein(0.5)
    .with_fadeout(0.5)
)

# -----------------------------
# COMPOSE FINAL VIDEO
# -----------------------------
final = CompositeVideoClip([bg, text_clip]).with_audio(final_audio)

# -----------------------------
# EXPORT
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
