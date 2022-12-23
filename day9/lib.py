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

    if abs(di) <= 1 and abs(dj) <= 1:
        return t

    # If in same row or column, we move if the difference is +/-2, not 1 or 0 (Assume it's never more than 2)
    if di == 0:
        return Point(t.i, t.j + dj // 2)
    if dj == 0:
        return Point(t.i + di // 2, t.j)

    # Diagonal move
    if abs(di) == 2 and abs(dj) == 1:
        return Point(t.i + di // 2, t.j + dj)
    if abs(dj) == 2 and abs(di) == 1:
        return Point(t.i + di, t.j + dj // 2)


def dump(h, t):
    mi = 6
    mj = 5
    [print("".join([point_str(h, t, i, j) for i in range(mi)]))
     for j in reversed(range(mj))]
    print()


def point_str(h, t, i, j):
    if h.match(i, j):
        return "H"
    elif t.match(i, j):
        return "T"
    else:
        return "."


def parse(line):
    direction, amount = re.search(r'(\w) (\d+)', line).groups()
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
