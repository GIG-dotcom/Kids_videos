import numpy as np
from scipy.io.wavfile import write
import os

os.makedirs("Music", exist_ok=True)

RATE = 44100
DURATION = 40
t = np.linspace(0, DURATION, int(RATE * DURATION), False)

tone = (
    np.sin(2 * np.pi * 220 * t) +
    np.sin(2 * np.pi * 330 * t)
) / 2

audio = np.int16(tone / np.max(np.abs(tone)) * 32767)

write("Music/background_music.wav", RATE, audio)

print("✅ Music/background_music.wav created")
