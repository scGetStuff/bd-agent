# cSpell:disable

# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


def main():
    # print(get_files_info("calculator", "."))
    # print(get_files_info("calculator", "pkg"))
    # print(get_files_info("calculator", "/bin"))
    # print(get_files_info("calculator", "../"))

    # doGetFile("calculator", "lorem.txt")
    # doGetFile("calculator", "main.py")
    # doGetFile("calculator", "pkg/calculator.py")
    # doGetFile("calculator", "/bin/cat")
    # doGetFile("calculator", "pkg/does_not_exist.py")

    # doWriteFile("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # doWriteFile("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # doWriteFile("calculator", "/tmp/temp.txt", "this should not be allowed")

    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))


def doGetFile(*args: str):
    err, stuff = get_file_content(*args)
    if err:
        print(err)
    else:
        print(stuff)


def doWriteFile(*args: str):
    print(write_file(*args))


if __name__ == "__main__":
    main()
