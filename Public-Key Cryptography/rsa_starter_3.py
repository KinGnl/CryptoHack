#!/bin/env sage

from sage.all import *

p = 857504083339712752489993810777

q = 1029224947942998075080348647219


def computer_phi(p, q):
    if (Integer(p).is_prime()):
        phi_p = p - 1
    else:
        phi_p = euler_phi(p)

    if (Integer(q).is_prime()):
        phi_q = q - 1
    else:
        phi_q = euler_phi(q)
    return phi_p * phi_q

print(computer_phi(p, q))
