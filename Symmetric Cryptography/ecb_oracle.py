from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

def decrypt():
    ciphertext = ""
    result = ""
    response = None
    j = 0
    flag = ""
    while(1):
        my_mes = ("A" * (31 - len(flag)))
        data = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/" + my_mes.encode().hex() + "/")
        ciphertext = data.text.split(':"')[1].split('"}')[0]
        ciphertext = bytes.fromhex(ciphertext)
        for i in range(32, 128):
            print(flag + chr(i))
            text = ("A" * (31 - len(flag))) + flag + chr(i)
            data = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/" + text.encode().hex() + "/")
            result = data.text.split(':"')[1].split('"}')[0]
            result = bytes.fromhex(result)
            if (ciphertext[16:32] == result[16:32]):
                flag += chr(i)
                break
        if (flag[-1] == '}'):
            break
        j += 1
    print(f"Congratulations ! This is your flag : {flag}")

decrypt()
