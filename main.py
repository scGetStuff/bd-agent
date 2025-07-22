import os
import sys
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    print("Hello from bd-agent!")

    words = readArgs()

    stuff = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=words,
        # contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )

    print(stuff.text)
    print(f"Prompt tokens: {stuff.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {stuff.usage_metadata.candidates_token_count}")


def readArgs():
    if len(sys.argv) != 2:
        print('Usage: uv run main.py "a bunch of words"')
        sys.exit(1)

    # "Why are episodes 7-9 so much worse than 1-6?"
    return sys.argv[1]


if __name__ == "__main__":
    main()
