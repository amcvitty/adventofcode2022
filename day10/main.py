from lib import *
import re
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


class CPU:
    def __init__(self):
        self.x = 1
        self.cycle = 1
        self.addnext = 0
        self.xs = [0]

    def do_tick(self, line):
        if line == "noop":
            self.tick()
        elif matches := re.search(r'addx ([\w-]+)', line):
            a = int(matches.groups()[0])
            self.tick()
            self.tick()
            self.x += a

    def tick(self):
        self.cycle += 1
        self.xs.append(self.x)


cpu = CPU()
for line in lines:
    line = line.strip()
    cpu.do_tick(line)


ss = [cpu.xs[c]*c for c in [20, 60, 100, 140, 180, 220]]

print(ss)
print(f"Part1: {sum(ss)}")

print(cpu.xs)
