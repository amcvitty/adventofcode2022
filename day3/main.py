import sys


def priority(item):
    if "a" <= item and item <= "z":
        return ord(common_item) - 96
    elif "A" <= item and item <= "Z":
        return ord(common_item) - 38
    else:
        raise Exception(f"Bad input to priority {item}")


# Part 1
with open(sys.argv[1]) as f:
    lines = f.readlines()

total = 0
for line in lines:
    line = line.strip()
    length = len(line)
    mid = int(length//2)
    first = line[0:mid]
    second = line[mid: length]
    # print(first)
    # print(second)
    common_item = [x for x in first if x in second][0]

    # print(f"{common_item}:{priority(common_item)}")

    total += priority(common_item)

print(f"Part 1: {total}")

total = 0
for i in range(0, len(lines)//3):
    line0 = lines[i*3].strip()
    line1 = lines[i*3 + 1].strip()
    line2 = lines[i*3 + 2].strip()
    common_item = [x for x in line0 if x in line1 and x in line2][0]
    print("For lines:")
    print(line0)
    print(line1)
    print(line2)

    print(f"{common_item}:{priority(common_item)}")

    total += priority(common_item)

print(f"Part 2: {total}")
