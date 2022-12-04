import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


scores = {"A": 1, "B": 2, "C": 3}
reverse_score = ["_", "A", "B", "C"]

total = 0
for line in lines:
    a, _, goal = line.strip()
    print(f"{a}-{goal}")
    opp_score = scores[a]
    score = 0
    if goal == "X":
        # lose by choosing number one less
        if opp_score == 1:
            score = 3
        else:
            score = opp_score - 1
    elif goal == "Y":
        # draw
        score = opp_score
        total += 3
    else:
        # win
        score = opp_score + 1
        total += 6
        if score > 3:
            score = 1

    print(f"Chose {reverse_score[score]}")

    total += score

print(total)
