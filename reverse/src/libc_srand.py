"""
Predict libc random values from known seed.

Category: Reverse Engineering

Description:
    Uses ctypes to call libc's srand and rand directly, allowing prediction
    of pseudo-random values when the seed is known from binary analysis.

Usage:
    python libc_srand.py

Dependencies:
    - ctypes (standard library)
    - Linux with libc.so.6
"""
import ctypes

srand = 0x1337
print(f"{srand=}")

libc = ctypes.CDLL("libc.so.6")
libc.srand(srand)
print(libc.rand() % 3)
