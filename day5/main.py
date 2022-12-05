import sys
import re
from lib import *

with open(sys.argv[1]) as f:
    lines = f.readlines()

stacks, commands = parse(lines)

for c in commands:
    execute_command(c, stacks)

part1 = "".join(stacks.peek_many(1, 10))
print(f"Part 1: { part1}")


stacks, commands = parse_inner(lines, Stacks9001())

for c in commands:
    execute_command(c, stacks)

part2 = "".join(stacks.peek_many(1, 10))
print(f"Part 2: { part2}")
