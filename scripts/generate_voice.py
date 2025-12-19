from gtts import gTTS
import os
import sys

story_file = "output/story.txt"
voice_file = "output/voice.wav"

os.makedirs("output", exist_ok=True)

if not os.path.exists(story_file):
    print("❌ story.txt not found")
    sys.exit(1)

with open(story_file, "r") as f:
    text = f.read().strip()

if not text:
    print("❌ story.txt is empty")
    sys.exit(1)

tts = gTTS(text=text, lang="en", slow=False)
tts.save(voice_file)

if not os.path.exists(voice_file):
    print("❌ Voice generation failed")
    sys.exit(1)

print("✅ Voice generated successfully:", voice_file)
