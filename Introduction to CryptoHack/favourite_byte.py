#!/bin/env python3



flag = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

i = 1
b = "\x00"

while(True):
    if (i ^ flag[0] == ord('c')):
        b = i
        break
    i += 1

print(f"The byte is {b}")
print("The flag is : ", "".join(chr(c ^ b) for c in flag))
