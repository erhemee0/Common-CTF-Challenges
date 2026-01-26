"""
Factor RSA modulus N when p and q are close using Fermat's method.

Category: Crypto > RSA

Description:
    When the two prime factors p and q of N are close to each other, Fermat's
    factorization method can efficiently find them. The algorithm searches for
    a and b such that N = a^2 - b^2 = (a+b)(a-b).

Usage:
    python fermats_factor_attack.py

Dependencies:
    - pycryptodome
    - gmpy2
"""
from Crypto.Util.number import long_to_bytes, inverse
from gmpy2 import isqrt, square, is_square

n = REDACTED
e = REDACTED
c = REDACTED

def fermat_factors(n):
    assert n % 2 != 0
    a = isqrt(n)
    b2 = square(a) - n
    while not is_square(b2):
        a += 1
        b2 = square(a) - n
    factor1 = a + isqrt(b2)
    factor2 = a - isqrt(b2)
    return int(factor1), int(factor2)

p, q = fermat_factors(n)
d = inverse(e, (p - 1) * (q - 1))
m = pow(c, d, n)

print(long_to_bytes(m))
