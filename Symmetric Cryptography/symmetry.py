#!/bin/env python3

import requests

def decrypt(encrypted):
    decrypted = ""
    encrypted = bytes.fromhex(encrypted)
    iv = encrypted[:16]
    flag = "crypto{"
    while (len(flag) != len(encrypted[16:])):
        for c in range(33, 128):
            data = requests.get("http://aes.cryptohack.org/symmetry/encrypt/" + (flag + chr(c)).encode().hex() + "/" + iv.hex() + "/")
            ciphertext = data.text.split(':"')[1].split('"}')[0]
            print(bytes.fromhex(ciphertext))
            print(encrypted[16:16+len(bytes.fromhex(ciphertext))])
            if (bytes.fromhex(ciphertext) == encrypted[16:16+len(bytes.fromhex(ciphertext))]):
                flag += chr(c)
                break
        print(flag)
            # print(ciphertext)
            # print(encrypted[16:].hex())
    # ciphertext = bytes.fromhex(ciphertext)
    return decrypted

encrypted = "a73171f79e30093632644971f906bbb503052268ea397c4f0d0c17c23a2d9b30d326905c42d515815f0ca91a8e4ac6150d"
decrypt(encrypted)
