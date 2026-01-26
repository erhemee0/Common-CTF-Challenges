"""
RSA attack when N is a perfect square (p = q).

Category: Crypto > RSA

Description:
    When RSA modulus N = p^2 (both primes are the same), phi(N) = p * (p - 1).
    Simply take the square root of N to find p and compute the private key.

Usage:
    python sqrted_n.py

Dependencies:
    - pycryptodome
    - gmpy2
"""
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes, inverse


n = 0xDEADBEEF
e = 0xDEADBEEF
c = 0xDEADBEEF

p = iroot(n, 2)
phi = p * (p - 1)
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
