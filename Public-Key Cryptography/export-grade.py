#!/bin/env sage

p = 0xde26ab651b92a129
g = 0x2
A = 0x88a63a7ca63a2622
B = 0x8a23ad70b6f8ec08
IV = "e80a06397afd9754bdde4e8c25e43dae"
encrypted_flag = "9ce036ebb64ab4863c69dca654a50aa073768a31aeeeff7177d6c0f3fefa00ea"

a = 0
b = 0

# print("A : ", A)
# print("B : ", B)
# print("g : ", g)
# print("p : ", p)

# https://www.alpertron.com.ar/DILOG.HTM
a = 6640353518945652322
b = 321403823798080866

s = pow(A, b, p)

print("Secret :", s)
print("IV: ", IV)
print("Encrypted flag: ", encrypted_flag)
# a_f = False
# b_f = False

# for i in range(p):
#     # print(i)
#     if (pow(g, i, p) == A):
#         print("a : ", i)
#         a_f = True
#     if (pow(g, i, p) == B):
#         print("b : ", i)
#         b_f = True
#     if (a_f and b_f):
#         break
