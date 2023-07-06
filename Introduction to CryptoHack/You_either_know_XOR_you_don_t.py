#!/bin/env python3

from pwn import *

flag = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

print(xor(flag[0:7], bytes("crypto{", "utf-8")))

# b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'

secret_flag = "myXORkey" * (len(flag) // 8)

print(xor(flag, bytes(secret_flag, "utf-8")))
