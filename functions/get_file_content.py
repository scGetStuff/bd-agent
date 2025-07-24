import os
from google.genai import types

MAX_CHARS = 10000


def get_file_content(working_directory, file_path) -> (str, str):

    try:
        workFullPath = os.path.abspath(working_directory)
        fileFullPath = os.path.abspath(os.path.join(workFullPath, file_path))

        if os.path.commonpath((workFullPath, fileFullPath)) != workFullPath:
            return (
                f'Error: Cannot read "{file_path}" as it is outside the permitted working directory',
                "",
            )

        if not os.path.isfile(fileFullPath):
            return (
                f'Error: File not found or is not a regular file: "{file_path}"',
                "",
            )

        with open(fileFullPath, "r") as f:
            fileContent = f.read(MAX_CHARS)

        if os.path.getsize(fileFullPath) > MAX_CHARS:
            fileContent += (
                f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            )

        return "", fileContent

    except Exception as e:
        return f"Error: {e}", ""


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Read the contents of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read, relative to the working directory.",
            ),
        },
    ),
)
