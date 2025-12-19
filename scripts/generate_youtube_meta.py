import os
import random

story_file = "output/story.txt"
meta_file = "output/youtube.txt"

if not os.path.exists(story_file):
    raise Exception("Story file not found")

with open(story_file, "r") as f:
    story = f.read().strip()

# Simple keyword pools
titles = [
    "Fun Story for Kids",
    "Kids Learning Story",
    "Cute Animal Story for Kids",
    "Moral Story for Children",
]

descriptions = [
    "A fun and simple story for kids to learn good habits.",
    "Watch this cute kids story and enjoy learning.",
    "A short and happy story for children.",
]

tags = [
    "#KidsStory",
    "#KidsLearning",
    "#CartoonStory",
    "#MoralStory",
    "#Shorts",
    "#KidsVideo"
]

title = random.choice(titles)
description = random.choice(descriptions)

content = f"""
TITLE:
{title}

DESCRIPTION:
{description}

STORY SUMMARY:
{story}

TAGS:
{" ".join(tags)}
"""

with open(meta_file, "w") as f:
    f.write(content.strip())

print("📝 YouTube metadata generated successfully")
print(content)
