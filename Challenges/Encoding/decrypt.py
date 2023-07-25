#!/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
import base64
import codecs

p = remote("socket.cryptohack.org", port=13377)


while (1):
    response = p.recvline().decode()
    type = ""
    encoded = ""
    decoded = ""
    if len(response.split(', ')) >= 2:
        type = response.split('",')[0].split(': "')[1]
        encoded = response.split('"encoded": ')[1].split('}')[0]
        print("type :", type)
        if type == "bigint":
            encoded = encoded.split('"')[1]
            encoded = encoded[2:]
            print("encoded :", encoded)
            decoded = bytes.fromhex(encoded).decode()
        if type == "utf-8":
            encoded = encoded.split('[')[1].split(']')[0].split(', ')
            for b in encoded:
                decoded += chr(int(b))
        if type == "hex":
            encoded = encoded.split('"')[1]
            print("encoded :", encoded)
            decoded = bytes.fromhex(encoded).decode()
        if type == "rot13":
            encoded = encoded.split('"')[1]
            print("encoded :", encoded)
            decoded = codecs.decode(encoded, "rot_13")
        if type == "base64":
            encoded = encoded.split('"')[1]
            print("encoded :", encoded)
            decoded = base64.b64decode(encoded).decode()
        print('{"decoded": ' + '"' + decoded + '"}')
        p.sendline(bytes('{"decoded": ' + '"' + decoded + '"}', encoding="utf-8"))
    else:
        print(response)

p.close()
