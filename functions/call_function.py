from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file


CWD = "./calculator"


def call_function(functionCall: types.FunctionCall, isVerbose=False) -> types.Content:
    if isVerbose:
        print(f"Calling function: {functionCall.name}({functionCall.args})")
    else:
        print(f" - Calling function: {functionCall.name}")

    functions = {
        "schema_get_files_info": schema_get_files_info,
        "schema_get_file_content": schema_get_file_content,
        "schema_run_python_file": schema_run_python_file,
        "schema_write_file": schema_write_file,
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
