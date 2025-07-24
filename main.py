import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
VERBOSE = "--verbose"
system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'


def main():
    print("Hello from bd-agent!")

    inputWords, isVerbose = readArgs()
    messages = [
        types.Content(role="user", parts=[types.Part(text=inputWords)]),
    ]
    cfg = types.GenerateContentConfig(system_instruction=system_prompt)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=cfg,
    )

    if isVerbose:
        print(f"User prompt: {inputWords}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Response:")
    print(response.text)


def readArgs() -> (str, bool):
    if len(sys.argv) < 2:
        print(f'Usage: uv run main.py "a bunch of words" <{VERBOSE}>')
        sys.exit(1)

    isVerbose = False
    if len(sys.argv) >= 3:
        isVerbose = sys.argv[2] == VERBOSE

    return sys.argv[1], isVerbose


if __name__ == "__main__":
    main()
