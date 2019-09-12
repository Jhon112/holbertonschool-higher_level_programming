#!/usr/bin/python3
from sys import argv
arguments = len(argv)
if __name__ == "__main__":
    if arguments == 1:
        print("0 arguments.")
    elif arguments == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arguments - 1))
        argument_list = argv[1:]
        for count, element in enumerate(argument_list, 1):
            print("{}: {}".format(count, element))
