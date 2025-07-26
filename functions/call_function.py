from google.genai import types
# from functions.get_files_info import schema_get_files_info
# from functions.get_file_content import schema_get_file_content
# from functions.run_python import schema_run_python_file
# from functions.write_file import schema_write_file

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


def call_function(functionCall: types.FunctionCall, isVerbose=False) -> types.Content:
    CWD = "./calculator"

    if isVerbose:
        print(f"Calling function: {functionCall.name}({functionCall.args})")
    else:
        print(f" - Calling function: {functionCall.name}")

    functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    f = functions.get(functionCall.name, None)
    if not f:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=functionCall.name,
                    response={"error": f"Unknown function: {functionCall.name}"},
                )
            ],
        )

    result = f(CWD, **functionCall.args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=functionCall.name,
                response={"result": result},
            )
        ],
    )
