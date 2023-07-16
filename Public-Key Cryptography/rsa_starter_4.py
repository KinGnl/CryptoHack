#!/bin/env sage

from sage.all import *

from rsa_starter_3 import computer_phi

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

e = 65537

d = inverse_mod(e, computer_phi(p, q))

print(d)
