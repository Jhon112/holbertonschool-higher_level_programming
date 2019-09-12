#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for el in dir(hidden_4):
        if "__" in el:
            continue
        print(el)
