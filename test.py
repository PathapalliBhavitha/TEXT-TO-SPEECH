from tts_engine import text_to_speech

def run_test(test_name, text):
    print(f"\n{'=' * 50}")
    print(f"Running Test: {test_name}")
    print(f"{'=' * 50}")

    try:
        # Condition 1: None Input
        if text is None:
            raise ValueError("Input cannot be None")

        # Condition 2: Empty or Whitespace Input
        if not str(text).strip():
            raise ValueError("Input text cannot be empty")

        # Condition 3: Very Large Input Warning
        if len(str(text)) > 5000:
            print("⚠ Warning: Extremely large input detected")

        # Execute TTS
        text_to_speech(str(text))

        print("✅ PASS - Audio generated successfully")

    except Exception as e:
        print(f"❌ FAIL - {e}")


# Test Cases stored in a list (Loop Testing)
test_cases = [
    ("Normal Input",
     "Hello, welcome to the Text To Speech project."),

    ("Empty Input",
     ""),

    ("Whitespace Input",
     "      "),

    ("Numeric Input",
     "1234567890"),

    ("Special Characters",
     "@#$%^&*()_+-=[]{}|;:',.<>?/"),

    ("Mixed Content",
     "Question 1: What is AI? Score = 95%"),

    ("Long Text Stress Test",
     "Artificial Intelligence is transforming industries. " * 100),

    ("Very Long Input Extreme Test",
     "Data " * 2000),

    ("Single Character",
     "A"),

    ("Repeated Character",
     "X" * 1000),

    ("None Input",
     None)
]

# Loop through all test cases
for test_name, test_input in test_cases:
    run_test(test_name, test_input)

print("\n🎯 All test cases executed.")
