import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

total = 0
results = []
for line in lines:
    if line.strip() != "":
        x = int(line)
        total += x
    else:
        results.append(total)
        total = 0

results.append(total)
total = 0
print(f"Part 1: {max(results)}")

results.sort(reverse=True)
part2 = sum(results[0:3])
print(f"Part 2: {part2}")
