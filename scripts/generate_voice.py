import subprocess
import os
import sys

story_file = "output/story.txt"
voice_file = "output/voice.wav"
model_file = "models/voice.onnx"

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Safety check
if not os.path.exists(story_file):
    print("❌ story.txt not found")
    sys.exit(1)

command = [
    "./piper/piper",
    "--model", model_file,
    "--output_file", voice_file
]

with open(story_file, "r") as f:
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        text=True
    )
    process.communicate(f.read())

# Final verification
if not os.path.exists(voice_file):
    print("❌ Voice generation failed, voice.wav not created")
    sys.exit(1)

print("✅ Voice generated successfully:", voice_file)
