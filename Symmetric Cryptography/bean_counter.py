#!/bin/env python3

from pwn import xor

f = open("./bean_counter_flag.txt", "r")
r = open("./flag.png", "wb")

content = f.read()
content = content.split()[0]
content = bytes.fromhex(content)
key = b""
png_header = bytes.fromhex("89504e470d0a1a0a0000000d49484452")
key = xor(content[:16], png_header)
b = b""

for i in range(0, len(content), 16):
    d = content[i:i+16]
    b += xor(d, key[:len(d)])

r.write(b)

f.close()
r.close()
