import os


def write_file(working_directory, file_path, content) -> str:
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
