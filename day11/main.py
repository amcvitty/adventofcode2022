
# Note to self! The part 1 and 2 were quite different, so to see part 1, go back in the git history


from lib import *
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

monkeys = Parser(lines).parse_all()
dump(monkeys)


for i in range(10000):
    for m, current_monkey in enumerate(monkeys):
        # print(f"Monkey {m+1}'s turn: ")

        while current_monkey.has_more():
            w, m = current_monkey.inspect_one()
            # print(f'Item with worry level {w} is passed to monkey {m}')
            monkeys[m].items.append(w)
    # print()
    # print(f"Round {i + 1}")
    # dump(monkeys)

inspections = [m.inspections for m in monkeys]
inspections.sort(reverse=True)
a, b, = inspections[:2]
print(f'Part1: {a*b}')
