import os
import sys
from typing import List, Tuple

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


def generate_content(
    client: genai.Client, messages: List[types.Content], isVerbose: bool
):  # pyright: ignore[reportUnknownParameterType]

    cfg = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,  # pyright: ignore[reportCallIssue]
    )

    modelResponse = (
        client.models.generate_content(  # pyright: ignore[reportUnknownMemberType]
            model="gemini-2.0-flash-001",
            contents=messages,
            config=cfg,
        )
    )

    if isVerbose:
        print(
            f"Prompt tokens: {modelResponse.usage_metadata.prompt_token_count}"  # pyright: ignore[reportOptionalMemberAccess]
        )
        print(
            f"Response tokens: {modelResponse.usage_metadata.candidates_token_count}"  # pyright: ignore[reportOptionalMemberAccess]
        )

    if not modelResponse.function_calls:
        return modelResponse.text

    funResponses: List[types.Part] = []
    for fun in modelResponse.function_calls:
        callContent = call_function(fun, isVerbose)

        if not callContent.parts or not callContent.parts[0].function_response:
            raise Exception("empty function call result")

        if isVerbose:
            print(f"-> {callContent.parts[0].function_response.response}")

        funResponses.append(callContent.parts[0])

    if not funResponses:
        raise Exception("no function responses generated, exiting.")


def readArgs() -> Tuple[str, bool]:

    if len(sys.argv) < 2:
        print(f'Usage: uv run main.py "a bunch of words" <{VERBOSE}>')
        sys.exit(1)

    isVerbose = False
    if len(sys.argv) >= 3:
        isVerbose = sys.argv[2] == VERBOSE

    return sys.argv[1], isVerbose


if __name__ == "__main__":
    main()
