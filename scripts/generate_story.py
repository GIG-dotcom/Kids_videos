# scripts/generate_story.py

import os
import requests
import re

# -----------------------------
# OUTPUT PATHS
# -----------------------------
OUTPUT_DIR = "output/story"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TITLE_FILE = f"{OUTPUT_DIR}/title.txt"
PART_FILES = [f"{OUTPUT_DIR}/part{i}.txt" for i in range(1, 6)]

# -----------------------------
# HUGGING FACE CONFIG
# -----------------------------
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

if not HF_API_TOKEN:
    raise Exception("❌ HF_API_TOKEN not found in environment")

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

# -----------------------------
# PROMPT
# -----------------------------
PROMPT = """
You are a friendly storyteller for kids aged 6 to 12.

Create ONE complete educational story told by a friendly animal named Nikki.

Rules:
- Language must be simple, fun, and friendly
- Short sentences
- No complex scientific words
- Nikki must speak directly to kids
- Nikki must appear in every part

Create exactly 5 connected parts for YouTube Shorts.

Structure:

Title: <short catchy title>

Part 1:
Nikki introduces herself and asks a curious question.

Part 2:
Nikki introduces the topic with a real-life example.

Part 3:
Nikki explains the main idea simply.

Part 4:
Nikki uses a fun analogy with toys, animals, games, or school.

Part 5:
Nikki gives a happy conclusion and encourages curiosity.

Choose a RANDOM kid-friendly topic (science, animals, space, nature, or daily life).
Do not mention being an AI.
"""

# -----------------------------
# CALL HUGGING FACE
# -----------------------------
response = requests.post(
    MODEL_URL,
    headers=HEADERS,
    json={"inputs": PROMPT, "parameters": {"max_new_tokens": 600}}
)

if response.status_code != 200:
    raise Exception(f"❌ Hugging Face API failed: {response.text}")

result = response.json()

if not isinstance(result, list):
    raise Exception("❌ Unexpected Hugging Face response")

text = result[0]["generated_text"]

# -----------------------------
# PARSE OUTPUT
# -----------------------------
title_match = re.search(r"Title:\s*(.*)", text)
parts = re.findall(r"Part\s*\d+:\s*(.*?)(?=Part\s*\d+:|$)", text, re.S)

if not title_match or len(parts) != 5:
    print(text)
    raise Exception("❌ AI output format invalid")

# -----------------------------
# SAVE FILES
# -----------------------------
with open(TITLE_FILE, "w") as f:
    f.write(title_match.group(1).strip())

for i, part in enumerate(parts):
    with open(PART_FILES[i], "w") as f:
        f.write(part.strip())

print("✅ Nikki story generated successfully")
