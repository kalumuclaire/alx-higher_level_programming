#!/usr/bin/python3
for c in range(0, 9):
    for a in range(c + 1, 10):
        if c == 8:
            print("{}{}".format(c, a))
        else:
            print("{}{}".format(c, a), end=", ")
