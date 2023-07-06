#!/bin/env python3

string = "label"

print("".join(chr(ord(c) ^ 13) for c in string))
