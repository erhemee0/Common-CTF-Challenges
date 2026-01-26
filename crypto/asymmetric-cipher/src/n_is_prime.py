"""
RSA edge case when N itself is prime.

Category: Crypto > RSA

Description:
    In rare cases, the modulus N might be prime instead of a product of two primes.
    When N is prime, phi(N) = N - 1, and decryption proceeds normally with this
    adjusted totient.

Usage:
    python n_is_prime.py

Dependencies:
    - pycryptodome
    - sympy
"""
from Crypto.Util.number import inverse, long_to_bytes
from sympy import isprime

n = 0xDEADBEEF
e = 0xDEADBEEF
c = 0xDEADBEEF

if not isprime(n):
    print("N is not prime number")
    exit()
d = inverse(e, n - 1)
m = pow(c, d, n)
print(long_to_bytes(m))
