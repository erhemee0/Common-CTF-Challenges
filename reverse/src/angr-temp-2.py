"""
Angr template for stdin-based challenges with charset constraints.

Category: Reverse Engineering

Description:
    Advanced angr template for binaries reading from stdin. Adds printable
    character constraints to symbolic variables and explores to success address.

Usage:
    python angr-temp-2.py

Dependencies:
    - angr
    - claripy
"""
from angr import Project
import claripy

SUCCESS     = 0x001046dd
FAIL        = 0x001046eb
BASE_ADDR   = 0x100000
FLAG_LEN    = 200
STDIN_FD    = 0

prj = Project('./rev', main_opts={'base_addr': BASE_ADDR})


flag_chars = [ claripy.BVS(f'flag_{_}', 8) for _ in range(FLAG_LEN) ]

flag = claripy.Concat( *flag_chars + [claripy.BVV('\n', 8)])

state = prj.factory.full_init_state(stdin=flag)

for _ in flag_chars:
    state.solver.add(_ >= ord('!'))
    state.solver.add(_ <= ord('~'))

simgr = prj.factory.simulation_manager(state)
simgr.explore(find=SUCCESS, avoid=FAIL)

print(f'[+] Found: {len(simgr.found)}')

if len(simgr.found) > 0:
    for _ in simgr.found:
        print(_.posix.dumps(STDIN_FD))
