import re
# grid is grid[row][col]


class Point():
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def match(self, i, j):
        return self.i == i and self.j == j

    def __repr__(self):
        return f"P({self.i},{self.j})"

    def __hash__(self):
        return f"P({self.i},{self.j})".__hash__()

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.i == other.i and self.j == other.j


def new_tail(h, t):
    di, dj = h.i - t.i, h.j - t.j

    # If only one away, don't move
    if abs(di) <= 1 and abs(dj) <= 1:
        return t

    # If in same row or column, we move if the difference is +/-2, not 1 or 0 (Assume it's never more than 2)
    if di == 0:
        return Point(t.i, t.j + dj // abs(dj))
    if dj == 0:
        return Point(t.i + di // abs(di), t.j)

    # Diagonal move

    return Point(t.i + di // abs(di), t.j + dj // abs(dj))
    if abs(dj) == 2 and abs(di) == 1:
        return Point(t.i + di, t.j + dj // 2)

    raise ValueError(f"Didn't find tail {h} {t}")


def dump(h, t):
    mi = 6
    mj = 5

    def point_str(h, t, i, j):
        if h.match(i, j):
            return "H"
        elif t.match(i, j):
            return "T"
        else:
            return "."

    [print("".join([point_str(h, t, i, j) for i in range(mi)]))
     for j in reversed(range(mj))]
    print()


def dump_rope(rope):

    def point_str(rope, i, j):
        ixs = [ix for ix, p in enumerate(rope) if p.i == i and p.j == j]
        if ixs:
            return str(min(ixs))
        elif i == 0 and j == 0:
            return "s"
        else:
            return "."
    dump_rope_int(rope, point_str)


def dump_tails(tails):

    def point_str(rope, i, j):
        ixs = [ix for ix, p in enumerate(rope) if p.i == i and p.j == j]
        if i == 0 and j == 0:
            return "s"
        elif ixs:
            return "*"
        else:
            return "."
    dump_rope_int(tails, point_str)


def dump_rope_int(rope, point_str):
    iis = list([x.i for x in rope]) + [0]
    jjs = list([x.j for x in rope]) + [0]
    min_i = min(iis)
    max_i = max(iis) + 1
    min_j = min(jjs)
    max_j = max(jjs) + 1

    [print("".join([point_str(rope, i, j) for i in range(min_i, max_i)]))
     for j in reversed(range(min_j, max_j))]
    print()


def parse(line):
    matches = re.search(r'(\w) (\d+)', line)
    if not matches:
        print(f"Couldn't match {line}")
        exit(1)
    direction, amount = matches.groups()
    match direction:
        case "R":
            di, dj = 1, 0
        case "L":
            di, dj = -1, 0
        case "U":
            di, dj = 0, 1
        case "D":
            di, dj = 0, -1
        case _:
            raise ValueError(direction)

    return di, dj, int(amount)
