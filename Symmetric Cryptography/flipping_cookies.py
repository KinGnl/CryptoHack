#!/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pwn import *
import requests

'''
    admin=False;expi
    ry={xxxxxxxxxxxx
    xxxxxxxxxxxxxxx}
'''

cookie = "ee8e4aad0af3b023dc96341630def62ecf2064a92be24d230f86081677dfa03b3a781aa15ea25666674f9a8eac876027"

'''
    We know that :
    d1 = c1 ^ iv
    Here d1 = 'admin=False;'
    We need to replace it by 'admin=True;'
    Sooooo, we need to got d2 = 'admin=True;'
    To null 'admin=False;' and the iv we need to XOR them
    To got 'admin=True;' we need to XOR it with the result of the previous computation
    To do so, we can operate through the iv:
    iv' = iv ^ 'admin=False;' ^ 'admin=True;'
'''

def decrypt(cookie):
    cookie = bytes.fromhex(cookie)
    iv = cookie[0:16]
    iv = xor(b"admin=True;aaaaa", xor(iv, b"admin=False;expi"))
    print(iv.hex())
    print(cookie[16:].hex())
    ### Let's crack the crack ###
    # key = "admin=True;expir".encode()
    # print(len(pad(key, 16)))

decrypt(cookie)
