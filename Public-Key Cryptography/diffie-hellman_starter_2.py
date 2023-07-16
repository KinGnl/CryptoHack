#!/bin/env python3

p = 28151

s = []

for g in range(p):
    for i in range(p):
        m = pow(g, i, p)
        if (m in s) == False:
            s.append(m)
    if len(s) == p - 1:
        print(g)
        break
    s = []
