#!/usr/bin/python3
from sys import argv
arguments = len(argv)
suma = 0
if __name__ == "__main__":
    if arguments == 1:
        print("{:d}".format(suma))
    else:
        for arg in argv[1:]:
            suma += int(arg)
        else:
            print(suma)
