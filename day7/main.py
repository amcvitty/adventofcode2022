import sys
# import re

from lib import *

with open(sys.argv[1]) as f:
    lines = f.readlines()

p = Parser(lines)
root = p.parse_directory("/")

# print(f'Directory {d.name} - {d.get_size()}'
print("Part 1: " + str(sum([d.get_size()
      for d in p.dirs if d.get_size() <= 100000])))

total_unused = 70000000 - root.get_size()
print(f'total_unused: {total_unused}')
target_to_free = 30000000 - total_unused
print(f'target: {target_to_free}')
part2 = min([d.get_size()
             for d in p.dirs if d.get_size() >= target_to_free])
print("Part 2: " + str(part2))
