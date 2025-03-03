import sys


def main():
    while True:
        sys.stdout.write("$ ")
        cmd = input()
        tok = cmd.split(" ")

        if tok[0] == "exit":
            if len(tok) > 1 and tok[1].isdigit():
                sys.exit(int(tok[1]))
            else:
                sys.exit()
        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
