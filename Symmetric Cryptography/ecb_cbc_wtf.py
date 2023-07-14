#!/bin/env python3

from pwn import xor
import requests

def decrypt(encrypted, decrypted):
    encrypted = bytes.fromhex(encrypted)
    decrypted = bytes.fromhex(decrypted)
    iv = encrypted[0:16]
    encrypted = encrypted[16:len(encrypted)]
    decrypted = decrypted[16:len(decrypted)]
    flag = b""
    for i in range(len(encrypted)//16):
        flag += xor(iv, decrypted[i*16:(i+1)*16])
        iv = encrypted[i*16:(i+1)*16]
    print(flag.decode())

encrypted = "5efb2ba85dfb4dfb491b5d575ed99e481f31cd1cdd076c9f419e4d2c73ea25a287f98517216b91aebbe466e07d6aab87"
decrypted = "03258b5ae8520cfb67e83c04e9f4a1903d8952d8299436c82a7902622bbaf57d4005bb2cec6333ae76c16c0d52cb04df"

decrypt(encrypted, decrypted)
