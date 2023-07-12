#!/bin/env python3

from sage.all import *

print(sage.arith.misc.crt([2, 3, 5], [5, 11, 17]))
print(Mod(872, 5))
print(Mod(872, 11))
print(Mod(872, 17))
print(Mod(872, 935))
