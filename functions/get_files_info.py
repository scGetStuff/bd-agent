import os


# TODO: mixing formatting with the data irritates me; should be split
def get_files_info(working_directory, directory=".") -> str:

    out = []

    s = f"'{directory}'"
    if directory == ".":
        s = "current"
    out.append(f"\nResult for {s} directory:")

    try:
        workFullPath = os.path.abspath(working_directory)
        dirFullPath = os.path.abspath(os.path.join(workFullPath, directory))

        if os.path.commonpath((workFullPath, dirFullPath)) != workFullPath:
            out.append(
                f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )
            return "\n    ".join(out)

        if not os.path.isdir(dirFullPath):
            out.append(f'Error: "{directory}" is not a directory')
            return "\n    ".join(out)

        for name in os.listdir(dirFullPath):
            path = os.path.join(dirFullPath, name)
            # print(f"PATH: {path}")
            out.append(
                f"{name}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}"
            )

        return "\n - ".join(out)

    except Exception as e:
        return f"Error: {e}"
