from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def main():
    # print(get_files_info("calculator", "."))
    # print(get_files_info("calculator", "pkg"))
    # print(get_files_info("calculator", "/bin"))
    # print(get_files_info("calculator", "../"))

    do(get_file_content, "calculator", "lorem.txt")
    do(get_file_content, "calculator", "main.py")
    do(get_file_content, "calculator", "pkg/calculator.py")
    do(get_file_content, "calculator", "/bin/cat")
    do(get_file_content, "calculator", "pkg/does_not_exist.py")


def do(f, *args):
    err, stuff = f(args[0], args[1])
    if err:
        print(err)
    else:
        print(stuff)


if __name__ == "__main__":
    main()
