from os.path import isdir
import subprocess
import sys
import os


def locate(os_path: str, filename: str) -> str | None:
    for path in os_path.split(":"):
        needle = f"{path}/{filename}"
        if os.path.isfile(needle):
            return needle
    return None


def main():
    while True:
        sys.stdout.write("$ ")
        istring = input()
        tok = istring.split(" ")
        cmd = tok[0]
        args = tok[1:]

        # exit
        if cmd == "exit":
            if len(args) > 0 and args[0].isdigit():
                sys.exit(int(args[0]))
            else:
                sys.exit()

        # echo
        if cmd == "echo":
            sys.stdout.write(" ".join(args) + "\n")
            continue

        # type
        if cmd == "type" and len(args) > 0:
            for e in args:
                if e == "echo":
                    print("echo is a shell builtin")
                elif e == "exit":
                    print("exit is a shell builtin")
                elif e == "type":
                    print("type is a shell builtin")
                else:
                    cmdpath = locate(str(os.getenv("PATH")), args[0])
                    if cmdpath is None:
                        print(f"{cmd} is unknown")
                    else:
                        print(f"{cmd} is {cmdpath}")
            continue

        # attempt to execute
        cmdpath = locate(str(os.getenv("PATH")), cmd)

        if cmdpath is None:
            print(f"{cmd}: command not found")
        else:
            rs = subprocess.run(cmdpath, capture_output=True, text=True)


if __name__ == "__main__":
    main()
