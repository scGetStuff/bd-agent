import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    print("Hello from bd-agent!")

    words = readArgs()
    messages = [
        types.Content(role="user", parts=[types.Part(text=words)]),
    ]

    stuff = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    print(stuff.text)
    print(f"Prompt tokens: {stuff.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {stuff.usage_metadata.candidates_token_count}")


def readArgs():
    if len(sys.argv) != 2:
        print('Usage: uv run main.py "a bunch of words"')
        sys.exit(1)

    return sys.argv[1]


if __name__ == "__main__":
    main()
