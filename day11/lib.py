import re


# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

class Parser:
    def __init__(self, lines):
        self.lines = lines
        self.ptr = 0

    def parse_all(self):
        monkeys = [self.parse_monkey()]
        while self.has_more():
            self.expect('^$')
            monkeys.append(self.parse_monkey())
        return monkeys

    def parse_monkey(self):
        self.expect(r'Monkey \d+:')

        items = re.findall(r'(\d+)', self.get_line())
        if not items:
            raise ValueError(f"didn't get items at line {self.ptr}")
        items = [int(i) for i in items]

        op, op2 = self.expect(r'Operation: new = old (.) (\w+)').groups()
        div_by = int(self.expect(r'Test: divisible by (\d+)').groups()[0])
        if_true = int(self.expect(
            r'If true: throw to monkey (\d+)').groups()[0])
        if_false = int(self.expect(
            r'If false: throw to monkey (\d+)').groups()[0])
        m = Monkey(items, op, op2, div_by, if_true, if_false)
        return m

    def expect(self, pattern):
        line = self.get_line()
        matches = re.search(pattern, line)
        if not matches:
            raise ValueError(
                f"Expected {pattern} but was {line} at line: {self.ptr - 1}")
        return matches

    def get_line(self):
        line = self.lines[self.ptr]
        self.ptr += 1
        return line

    def peek_line(self):
        return self.lines[self.ptr]

    def has_more(self):
        return self.ptr < len(self.lines)


class Monkey:
    def __init__(self, items, op, op2, div_by, if_true, if_false):
        self.items = items
        self.op = op
        self.op2 = op2
        self.div_by = div_by
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def inspect_one(self):
        self.inspections += 1
        x = self.items.pop(0)
        # print(f'Monkey inspects an item with a worry level of {x}.  ')
        if self.op2 == 'old':
            y = x
        else:
            y = int(self.op2)

        if self.op == '*':
            x *= y
        elif self.op == '+':
            x += y
        else:
            raise ValueError(f'No op for {self.op}')

        x = x // 3

        if x % self.div_by == 0:
            return x, self.if_true
        else:
            return x, self.if_false

    def has_more(self):
        return len(self.items) > 0


def dump(monkeys):
    for i, m in enumerate(monkeys):
        print(f'Monkey {i}: {m.items}. {m.inspections}')
