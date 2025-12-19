import os
import subprocess

story_file = "output/story.txt"
voice_file = "output/voice.wav"

if not os.path.exists(story_file):
    raise Exception("Story file not found")

os.makedirs("output", exist_ok=True)

# Read story text
with open(story_file, "r") as f:
    text = f.read()

# Generate voice using eSpeak
command = [
    "espeak-ng",
    "-s", "140",      # speed (kids-friendly)
    "-p", "60",       # pitch
    "-w", voice_file,
    text
]

subprocess.run(command, check=True)

print("✅ Voice generated successfully:", voice_file)
