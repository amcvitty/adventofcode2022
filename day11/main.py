from lib import *
import re
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

monkeys = Parser(lines).parse_all()


for i in range(20):
    for current_monkey in monkeys:
        while current_monkey.has_more():
            w, m = current_monkey.inspect_one()
            # print(f'Item with worry level {w} is passed to monkey {m}')
            monkeys[m].items.append(w)
    print()
    print(f"Round {i + 1}")
    dump(monkeys)

inspections = [m.inspections for m in monkeys]
inspections.sort(reverse=True)
a, b, = inspections[:2]
print(inspections)
print(f'Part1: {a*b}')
