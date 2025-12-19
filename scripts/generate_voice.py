import subprocess
import os
import sys

story_file = "output/story.txt"
voice_file = "output/voice.wav"
model_file = "models/voice.onnx"
config_file = "models/voice.onnx.json"

os.makedirs("output", exist_ok=True)

# Safety checks
for f in [story_file, model_file, config_file]:
    if not os.path.exists(f):
        print(f"❌ Missing required file: {f}")
        sys.exit(1)

command = [
    "./piper/piper",
    "--model", model_file,
    "--config", config_file,
    "--output_file", voice_file
]

with open(story_file, "r") as f:
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        text=True
    )
    process.communicate(f.read())

if not os.path.exists(voice_file):
    print("❌ Voice generation failed")
    sys.exit(1)

print("✅ Voice generated successfully:", voice_file)
