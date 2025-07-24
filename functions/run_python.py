import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        workFullPath: str = os.path.abspath(working_directory)
        fileFullPath: str = os.path.abspath(os.path.join(workFullPath, file_path))

        if os.path.commonpath((workFullPath, fileFullPath)) != workFullPath:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(fileFullPath):
            return f'Error: File "{file_path}" not found.'

        if fileFullPath[-3].lower() == ".py":
            return f'Error: "{file_path}" is not a Python file.'

        line = " ".join(["uv", "run", file_path] + args)
        # print(line)

        cp = subprocess.run(
            line,
            shell=True,
            cwd=workFullPath,
            capture_output=True,
            timeout=30,
        )

        print(f"STDOUT: {cp.stdout}")
        print(f"STDERR: {cp.stderr}")
        if cp.returncode != 0:
            print(f"Process exited with code {cp.returncode}")
        if cp.stdout == "":
            print("No output produced")

        return ""

    except Exception as e:
        return f"Error: executing Python file: {e}"
