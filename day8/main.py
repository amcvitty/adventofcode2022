import sys
# import re

from lib import *

with open(sys.argv[1]) as f:
    lines = f.readlines()

grid = [[int(d) for d in line.strip()] for line in lines]
# print(grid)
visible = [[0 for col in row] for row in grid]
# print(visible)

# Start from left in top row
for i in range(len(grid)):
    max_size = -1
    for j in range(len(grid[i])):
        if grid[i][j] > max_size:
            max_size = grid[i][j]
            visible[i][j] = 1

# And from right
for i in range(len(grid)):
    max_size = -1
    for j in reversed(range(len(grid[i]))):
        if grid[i][j] > max_size:
            max_size = grid[i][j]
            visible[i][j] = 1

# Start from top
for j in range(len(grid[0])):
    max_size = -1
    for i in range(len(grid)):
        if grid[i][j] > max_size:
            max_size = grid[i][j]
            visible[i][j] = 1

for j in range(len(grid[0])):
    max_size = -1
    for i in reversed(range(len(grid))):
        if grid[i][j] > max_size:
            max_size = grid[i][j]
            visible[i][j] = 1
# print(visible)
print("Part 1: " + str(sum([sum(row) for row in visible])))

print("Part 2: " + str(max([max([score(grid, i, j) for j in range(len(grid[i]))])
      for i in range(len(grid))])))
