import os
from google.genai import types


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        workFullPath = os.path.abspath(working_directory)
        fileFullPath = os.path.abspath(os.path.join(workFullPath, file_path))

        if os.path.commonpath((workFullPath, fileFullPath)) != workFullPath:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(fileFullPath):
            os.makedirs(os.path.dirname(fileFullPath), exist_ok=True)
        with open(fileFullPath, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Write the content to file_path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to file_path, relative to the working directory.",
            ),
        },
    ),
)
