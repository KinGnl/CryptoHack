#!/bin/env python3
# from sage.all import *
from factordb.factordb import FactorDB
import random
from Crypto.Util.number import *

p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff

g = 0x02

original_A = 0xc257393104102a606716e4197b20be4ce5af5e11bc941e0dd8660b4dfd36b6d93ce05fd173ba4db4027c20af482148ed46e102c1087fb527b549d9c045bf7521a8aa6eece312e2854474423d529c86b322ae92559faac8f5ffd1f4c6962fb4c1d51fa1680cecc05a715ef7efb437b7a11a8e009c11f5efde4e7657b9d4108c5b744e0e139300492c0c4fdb657993ee1e78679747a4cb87423acb51b26ddb6ef966a978e02d5b3321f4383681104da22a93d367428a0e846f7b35337cf02cddb9

alice_key1 = random.randint(2, p-1)
bob_key1 = random.randint(2, p-1)

alice_pub1 = pow(g, alice_key1, p)
bob_pub1 = pow(g, bob_key1, p)

secret = pow(original_A, bob_key1, p)


print("New Alice: ", long_to_bytes(alice_pub1).hex())
print("New Bob : ", long_to_bytes(bob_pub1).hex())
print("New Secret :", secret)

# iv = "127a2d385ad419c1cd512a3bcd8fe328"
# encrypted_flag = "ec93b30bb4a0d49feb65aeec9e5ffadb3efeea55b72bf292c29495ca3c55474b"

# print("Shared Secret :", secret)
# print("IV : ", iv)
# print("ENCRYPTED_FLAG", encrypted_flag)

# bob_pub = 0x21c04184453fc57cdfb66262eb1fc6e8e3219f3671553fd55ba340009ac0c68225f4c8a3e533911d1dd90cf9f32ddece0a52901b43980fba18996b38a7dd92f5286f1a43d79588ea6be87fa350ee4e0b10cc942587cf75007843855e8eb42e4a6f8bc08c31f5738cd176c046fddf7b0216d128bfc3204ff1629e290b629194d801bba2ac74b0ce04028a9eedf83ff8f5c127e1af92fdaafa66ca7bd6b7dbf62564daec057ab5c57110113d3c170709c951e15d2552332ee7cbcc22d94e17ec9a


# iv = "071cad9319490ea7489f5c86fc6cfe7c"
# encrypted_flag = "6a85aa37653348e332cca7e520f04c25312c1cba61a5153ffc189a6f36b5b882"
# # encrypted_flag = "a68aaaf3da4842be2004eb5246eeca3a9b28bc6163a982ab532cef3dfeeaa110"

# print("iv : ", iv)
# print("encrypted_flag: ", encrypted_flag)
# print("secret: ", secret)
