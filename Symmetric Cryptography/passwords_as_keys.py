
from Crypto.Cipher import AES
import hashlib
import random

ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words

# KEY = hashlib.md5(keyword.encode()).digest()

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}

plaintext = ""

alright = True
with open("/usr/share/dict/words") as f:
    for w in f.readlines():
        keyword = w.strip()
        KEY = hashlib.md5(keyword.encode()).digest().hex()
        plaintext = bytes.fromhex(decrypt(ciphertext, KEY)["plaintext"])
        for b in plaintext:
            if b < 32 or b > 127:
                alright = False
                break
        if (alright == True):
            print(plaintext.decode())
        alright = True
