#!/bin/env sage

from sage.all import *

p = 29
ints = [14, 6, 11]

q_r = quadratic_residues(p)

for i in ints:
    if (i in q_r):
        print(-i, i)
        break
