#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = 1
    arg_num = len(sys.argv) - 1
    if arg_num > 0:
        print("{} arguments:".format(arg_num))
    else:
        print("{} arguments.".format(arg_num))
    for args in sys.argv[1:]:
        print("{}: {}".format(a, args))
        a += 1
