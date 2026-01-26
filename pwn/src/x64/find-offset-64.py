"""
x64 buffer overflow offset finder using cyclic pattern.

Category: Pwn > Buffer Overflow

Description:
    Automatically finds the offset to RIP/return address using pwntools
    cyclic pattern and core dump analysis. Essential first step for BOF exploits.

Usage:
    python find-offset-64.py

Dependencies:
    - pwntools
"""
from pwn import *

elf = context.binary = ELF('challenge', checksec=False)

context.log_level = 'debug'

io = process(elf.path)

io.sendline(cyclic(128))
io.wait()

core = io.corefile
stack = core.rsp
pattern = core.read(stack, 4)

success(f"Pattern: {pattern.decode()}")
success(f'Offset: {cyclic_find(pattern)}')
