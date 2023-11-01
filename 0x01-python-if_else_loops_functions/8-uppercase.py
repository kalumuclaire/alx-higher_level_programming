#!/usr/bin/python3
def uppercase(str):
    for d in str:
        if ord(d) >= ord('a') and ord(d) <= ord('z'):
            char = chr(ord(d) - 32)
        else:
            char = d
        print("{:s}".format(char), end="")
    print('')
