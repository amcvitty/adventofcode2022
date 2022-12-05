import re


class Stacks:

    def __init__(self):
        self.s = [[] for x in range(0, 10)]

    def push(self, i, x):
        self.s[i].append(x)

    def pop(self, i):
        return self.s[i].pop()

    def peek(self, i):
        return self.s[i][-1]

    def peek_many(self, a, z):
        return [stack[-1] if len(stack) > 0 else "" for stack in self.s[a: z]]

    def unshift(self, i, x):
        self.s[i].insert(0, x)

    def move(self, times, from_stack, to_stack):
        for i in range(0, times):
            self.s[to_stack].append(self.s[from_stack].pop())

    def __str__(self):
        return "\n".join([f"{i}: {str(x)}" for i, x in enumerate(self.s)])


class Stacks9001(Stacks):

    def move(self, times, from_stack, to_stack):
        temp_stack = []

        for i in range(0, times):
            temp_stack.append(self.s[from_stack].pop())
        for i in range(0, times):
            self.s[to_stack].append(temp_stack.pop())


def maybe_insert(line, i, s, si):
    if len(line) > i and line[i] != " ":
        s.unshift(si, line[i])


def parse(lines):
    return parse_inner(lines, Stacks())


def parse_inner(lines, s):
    row = 0

    line = lines[0]
    while line[1] != "1":
        for c in range(0, 9):
            maybe_insert(line, c*4 + 1, s, c+1)
        row += 1
        line = lines[row]

    commands = [parse_command(line) for line in lines[row+1:] if len(line) > 3]
    return [s, commands]


def parse_command(line):
    return [int(x) for x in re.search(r'move (\d+) from (\d+) to (\d+)', line).groups()]


def execute_command(command_tuple, stacks):
    """
     command in the form [1 (times ),2 (from stack),4 (to_stack)]
    """
    times, from_stack, to_stack = command_tuple
    stacks.move(times, from_stack, to_stack)
