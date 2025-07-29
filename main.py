import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from functions.call_function import call_function, available_functions


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
VERBOSE = "--verbose"


def main():
    print("Hello from bd-agent!")

    inputWords, isVerbose = readArgs()
    messages = [
        types.Content(role="user", parts=[types.Part(text=inputWords)]),
    ]

    generate_content(client, messages, isVerbose)


def generate_content(client, messages, isVerbose):

    cfg = types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    modelResponse = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=cfg,
    )

    if isVerbose:
        print(f"Prompt tokens: {modelResponse.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {modelResponse.usage_metadata.candidates_token_count}")

    for fun in modelResponse.function_calls:
        callContent = call_function(fun, isVerbose)
        funResult = callContent.parts[0].function_response.response

        if funResult is None:
            print(f"Executing {fun.name} did bad stuff")
            sys.exit(1)

        if isVerbose:
            # print(f"-> {funResult.get("result", "")}")
            print(f"-> {funResult}")

    if len(modelResponse.function_calls) == 0:
        print("Response:")
        print(modelResponse.text)


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
