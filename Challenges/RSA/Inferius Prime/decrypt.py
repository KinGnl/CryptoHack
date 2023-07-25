#!/bin/env python3

from factordb.factordb import FactorDB
from primefac import *
from Crypto.Util.number import *

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

f = FactorDB(n)
f.connect()
primes = f.get_factor_list()
phi = 1

for p in primes:
    phi *= p - 1

d = modinv(e, phi)

print(long_to_bytes(pow(ct, d, n)).decode())
