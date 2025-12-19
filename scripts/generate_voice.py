from piper import PiperVoice
import os
import sys

story_file = "output/story.txt"
voice_file = "output/voice.wav"

os.makedirs("output", exist_ok=True)

if not os.path.exists(story_file):
    print("❌ story.txt missing")
    sys.exit(1)

with open(story_file, "r") as f:
    text = f.read()

# Load built-in English voice (safe & stable)
voice = PiperVoice.load("en_US-lessac-medium")

with open(voice_file, "wb") as f:
    voice.synthesize(text, f)

if not os.path.exists(voice_file):
    print("❌ Voice generation failed")
    sys.exit(1)

print("✅ Voice generated successfully:", voice_file)
