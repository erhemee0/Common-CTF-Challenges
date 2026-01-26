"""
Wiener's attack on RSA when d is small relative to N.

Category: Crypto > RSA

Description:
    When the private exponent d is small (d < N^0.25 / 3), Wiener's attack uses
    continued fractions to recover d from the public key (e, N). This script
    uses the owiener library for the attack.

Usage:
    python wiener_attack.py

Dependencies:
    - pycryptodome
    - owiener
"""
from owiener import attack
from Crypto.Util.number import long_to_bytes

n = 0xDEADBEEF
e = 0xDEADBEEF
c = 0xDEADBEEF
d = attack(e, n)

if d:
    print(long_to_bytes(pow(c, d, n)).decode())
else:
    print('No luck!')
