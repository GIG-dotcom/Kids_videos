from moviepy import ColorClip, concatenate_videoclips
import os

os.makedirs("assets", exist_ok=True)

WIDTH, HEIGHT = 720, 1280
DURATION = 40  # seconds

colors = [
    (135, 206, 235),  # sky blue
    (144, 238, 144),  # light green
    (255, 182, 193),  # light pink
]

clips = [
    ColorClip(size=(WIDTH, HEIGHT), color=c).with_duration(DURATION / len(colors))
    for c in colors
]

final = concatenate_videoclips(clips)

final.write_videofile(
    "assets/background.mp4",
    fps=24,
    codec="libx264",
    audio=False
)

print("✅ assets/background.mp4 created successfully")
