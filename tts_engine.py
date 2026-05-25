from gtts import gTTS
from playsound import playsound
import os
from config import LANGUAGE, SLOW, OUTPUT_FILE

def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang=LANGUAGE, slow=SLOW)

        os.makedirs("output", exist_ok=True)

        tts.save(OUTPUT_FILE)

        print(f"Audio saved at: {OUTPUT_FILE}")

        playsound(OUTPUT_FILE)

    except Exception as e:
        print("Error:", e)