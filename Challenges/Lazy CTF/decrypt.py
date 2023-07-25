#!/bin/env python3

import requests
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from pwn import *

# print(xor(bytes.fromhex("00000000000000000000000000000000"), b"abcd"))
# plaintext = "8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c"
# # plaintext = bytes(plaintext, encoding="utf-8").hex()

# for i in range(1, 127):
#     print(bytes([i]).hex() + plaintext[2:])
#     data = requests.get("http://aes.cryptohack.org/lazy_cbc/encrypt/" + bytes([i]).hex() + plaintext[2:] + "/")
#     ciphertext = data.text.split(':"')[1].split('"}')[0]
#     # print(bytes.fromhex(len(ciphertext), ciphertext))

#     data = requests.get("http://aes.cryptohack.org/lazy_cbc/receive/" + ciphertext + "/")
#     plaintext_received = data.text.split(':')[2].split('"}')[0]

#     print("*" + "-" * 40 + "*")
#     print("Ciphertext : ", ciphertext, "Length : ", len(bytes.fromhex(ciphertext)))
#     print("Plaintext : ", plaintext_received, "Length : ", len(bytes.fromhex(plaintext_received)))
#     print(len(ciphertext) < len(plaintext_received))
#     print("*" + "-" * 40 + "*")

ciphertext = bytes.fromhex("d735de4e1197d0a1bd8878978f96edbf")

cipher = AES.new(ciphertext, AES.MODE_CBC, ciphertext)

encrypted = "00000000000000000000000000000000"

text = cipher.decrypt(ciphertext)
print(text.hex())
