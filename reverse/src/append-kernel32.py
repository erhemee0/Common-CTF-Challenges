"""
Append kernel32.dll to PE for UPX unpacking issues.

Category: Reverse Engineering

Description:
    Some UPX-packed executables fail to unpack if kernel32.dll is missing
    or truncated. This script appends kernel32.dll to the binary to fix
    unpacking issues.

Usage:
    python append-kernel32.py

Dependencies:
    - None (standard library only)
"""
filename = 'changeme.exe'

with open(filename, 'ab') as a, open('kernel32.dll', 'rb') as b:
    a.write(b.read())
