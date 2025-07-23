import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path) -> (str, str):

    try:
        workFullPath = os.path.abspath(working_directory)
        # print(f"workFullPath: {workFullPath}")
        fileFullPath = os.path.abspath(os.path.join(workFullPath, file_path))
        # print(f"fileFullPath: {fileFullPath}")

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
            fileContent += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return "", fileContent

    except Exception as e:
        return f"Error: {e}", ""
