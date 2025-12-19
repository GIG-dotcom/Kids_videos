from PIL import Image, ImageDraw
import os
import random

os.makedirs("output", exist_ok=True)

width, height = 720, 1280
colors = [(255, 200, 200), (200, 255, 200), (200, 200, 255)]

for i in range(1, 6):
    img = Image.new("RGB", (width, height), random.choice(colors))
    draw = ImageDraw.Draw(img)

    draw.text((180, 600), f"Kids Story {i}", fill=(0, 0, 0))

    img.save(f"output/img_0{i}.png")

print("✅ Images generated")
print("✅ Images generated successfully")
