import subprocess
import os

story_file = "output/story.txt"
voice_file = "output/voice.wav"
model_file = "models/voice.onnx"

with open(story_file, "r") as f:
    text = f.read()

command = [
    "./piper/piper",
    "--model", model_file,
    "--output_file", voice_file
]

process = subprocess.Popen(
    command,
    stdin=subprocess.PIPE,
    text=True
)

process.communicate(text)

print("✅ Natural voice generated")
