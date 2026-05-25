from tts_engine import text_to_speech

def main():
    print("=== TEXT TO SPEECH SYSTEM ===")

    text = input("Enter text: ")

    if text.strip() == "":
        print("Text cannot be empty")
        return

    text_to_speech(text)

if __name__ == "__main__":
    main()