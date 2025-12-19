from PIL import Image, ImageDraw, ImageFont
import os
import random

os.makedirs("output", exist_ok=True)

width, height = 720, 1280  # Shorts size
backgrounds = [
    (135, 206, 235),  # sky blue
    (255, 228, 181),  # light yellow
    (204, 255, 204),  # light green
]

texts = [
    "Hello Kids!",
    "Let's Learn",
    "Have Fun!",
]

for i in range(1, 4):
    img = Image.new("RGB", (width, height), random.choice(backgrounds))
    draw = ImageDraw.Draw(img)

    # Draw ground
    draw.rectangle([0, 900, width, height], fill=(34, 139, 34))

    # Draw simple animal (circle face)
    draw.ellipse([260, 400, 460, 600], fill=(255, 224, 189))
    draw.ellipse([300, 460, 320, 480], fill=(0, 0, 0))
    draw.ellipse([400, 460, 420, 480], fill=(0, 0, 0))
    draw.arc([330, 500, 390, 540], start=0, end=180, fill=(0, 0, 0), width=3)

    # Big text
    draw.text((200, 200), texts[i-1], fill=(0, 0, 0))

    img.save(f"output/img_0{i}.png")

print("✅ Images generated successfully")
