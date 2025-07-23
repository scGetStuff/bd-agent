# cSpell:disable

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


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

    doWriteFile("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    doWriteFile("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    doWriteFile("calculator", "/tmp/temp.txt", "this should not be allowed")


def doGetFile(*args):
    err, stuff = get_file_content(*args)
    if err:
        print(err)
    else:
        print(stuff)


def doWriteFile(*args):
    print(write_file(*args))


if __name__ == "__main__":
    main()
