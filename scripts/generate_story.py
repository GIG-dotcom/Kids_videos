import random
import os

characters = ["Elephant", "Rabbit", "Monkey", "Panda", "Lion"]
lessons = ["kindness", "sharing", "helping friends", "learning numbers", "being honest"]

character = random.choice(characters)
lesson = random.choice(lessons)

story = f"""
Once upon a time, there was a happy {character}.

The {character} went to play and learned about {lesson}.
Everyone smiled and felt very happy.

The end.
"""

os.makedirs("output", exist_ok=True)

with open("output/story.txt", "w") as f:
    f.write(story.strip())

print("✅ Story generated")
