from PIL import Image, ImageDraw, ImageFont
import os
import random

os.makedirs("output", exist_ok=True)

WIDTH, HEIGHT = 720, 1280

backgrounds = [
    (255, 204, 204),  # pink
    (204, 255, 204),  # green
    (204, 204, 255),  # blue
    (255, 255, 204),  # yellow
    (255, 204, 255),  # purple
]

emojis = ["🐘", "🐰", "🐵", "🐼", "🦁"]

texts = [
    "Hello Kids!",
    "Let’s Learn Together",
    "Be Kind ❤️",
    "Share With Friends 🤝",
    "The End 😊"
]

try:
    font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", 90)
    font_small = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
except:
    font_big = font_small = ImageFont.load_default()

for i in range(5):
    img = Image.new("RGB", (WIDTH, HEIGHT), random.choice(backgrounds))
    draw = ImageDraw.Draw(img)

    emoji = random.choice(emojis)
    text = texts[i]

    # Emoji (top)
    draw.text((WIDTH // 2 - 50, 200), emoji, font=font_big, fill=(0, 0, 0))

    # Text (center) – FIXED
    bbox = draw.textbbox((0, 0), text, font=font_small)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    draw.text(
        ((WIDTH - text_w) // 2, HEIGHT // 2),
        text,
        font=font_small,
        fill=(0, 0, 0)
    )

    # Footer
    footer = "Kids Story Time"
    footer_bbox = draw.textbbox((0, 0), footer, font=font_small)
    footer_w = footer_bbox[2] - footer_bbox[0]

    draw.text(
        ((WIDTH - footer_w) // 2, HEIGHT - 200),
        footer,
        font=font_small,
        fill=(0, 0, 0)
    )

    img.save(f"output/img_0{i+1}.png")

print("✅ High-quality cartoon images generated")
