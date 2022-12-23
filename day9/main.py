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

# print("Part 2: " + str(max([max([score(grid, i, j) for j in range(len(grid[i]))])
#       for i in range(len(grid))])))
