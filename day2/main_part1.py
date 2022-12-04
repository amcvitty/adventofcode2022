import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


scores = {"X": 1, "Y": 2, "Z": 3,
          "A": 1, "B": 2, "C": 3}

total = 0
for line in lines:
    a, _, me = line.strip()
    print(f"{a}-{me}")

    total += scores[me]

    if (scores[me] - scores[a]) % 3 == 1:
        print("Win")
        total += 6
    elif scores[me] == scores[a]:
        print("Draw")
        total += 3
    else:
        print("Lose")


# results.append(total)
# total = 0
# print(f"Part 1: {max(results)}")

# results.sort(reverse=True)
# part2 = sum(results[0:3])
# print(f"Part 2: {part2}")
print(total)
