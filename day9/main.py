import sys
# import re

from lib import *


with open(sys.argv[1]) as f:
    lines = f.readlines()

# initial state
h = t = Point(0, 0)
print("== Initial State ==")
dump(h, t)

tails = set()

for line in lines:
    di, dj, amount = parse(line)
    print(f"########## {line.strip()} ##########")
    for x in range(amount):
        h = Point(h.i + di, h.j + dj)
        t = new_tail(h, t)
        tails.add(t)
        # dump(h, t)


print("Part 1: " + str(len(tails)))


# initial state
rope = [Point(0, 0) for _ in range(10)]
print("== Initial State ==")
dump_rope(rope)
tails = set()
for line in lines:
    di, dj, amount = parse(line)
    print(f"########## {line.strip()} ##########")
    for x in range(amount):
        rope[0] = Point(rope[0].i + di, rope[0].j + dj)
        for n in range(1, len(rope)):
            rope[n] = new_tail(rope[n-1], rope[n])
        tails.add(rope[-1])
        # dump_rope(rope)


# dump_tails(list(tails))
print("Part 2: " + str(len(tails)))
