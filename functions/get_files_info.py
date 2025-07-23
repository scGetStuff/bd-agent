import os




# TODO: mixing formatting with the data irritates me; should be split
def get_files_info(working_directory, directory=".") -> str:

    out = []

    s = f"'{directory}'"
    if directory == ".":
        s = "current"
    out.append(f"\nResult for {s} directory:")

    try:
        working_directory = os.path.abspath(working_directory)
        # print(f"working_directory: {working_directory}")
        fullPath = os.path.abspath(os.path.join(working_directory, directory))
        # print(f"fullPath: {fullPath}")

        # print(f"before commonpath: \n\t{working_directory}\n\t{fullPath}")
        if os.path.commonpath((working_directory, fullPath)) != working_directory:
            out.append(
                f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )
            return "\n    ".join(out)

        if not os.path.isdir(fullPath):
            out.append(f'Error: "{directory}" is not a directory')
            return "\n    ".join(out)

        for name in os.listdir(fullPath):
            path = os.path.join(fullPath, name)
            # print(f"PATH: {path}")
            out.append(
                f"{name}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}"
            )

        return "\n - ".join(out)

    except Exception as e:
        return f"Error: {e}"
