import sys
import re


def contains(a1, a2, b1, b2):
    return a1 <= b1 and a2 >= b2


def overlaps(a1, a2, b1, b2):
    return a1 <= b1 and b1 <= a2 or a1 <= b2 and b2 <= a2


with open(sys.argv[1]) as f:
    lines = f.readlines()

containing_count = 0
overlap_count = 0
for line in lines:
    a, b = line.strip().split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    if contains(a1, a2, b1, b2) or contains(b1, b2, a1, a2):
        print(a1, a2, b1, b2)
        containing_count += 1
    if overlaps(a1, a2, b1, b2) or overlaps(b1, b2, a1, a2):
        print(a1, a2, b1, b2)
        overlap_count += 1

print(f"Part 1: {containing_count}")
print(f"Part 2: {overlap_count}")
