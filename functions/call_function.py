from types import FunctionType
from typing import Dict, Any
from google.genai import types

from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python import run_python_file, schema_run_python_file


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
CWD = "./calculator"


def call_function(
    functionCall: types.FunctionCall, isVerbose: bool = False
) -> types.Content:

    if isVerbose:
        print(f"Calling function: {functionCall.name}({functionCall.args})")
    else:
        print(f" - Calling function: {functionCall.name}")

    functions: Dict[str, FunctionType] = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    f = functions.get(functionCall.name, None)  # type: ignore
    if not f:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=functionCall.name,  # type: ignore
                    response={"error": f"Unknown function: {functionCall.name}"},
                )
            ],
        )

    result: Any = f(CWD, **functionCall.args)  # type: ignore

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=functionCall.name,  # type: ignore
                response={"result": result},
            )
        ],
    )
