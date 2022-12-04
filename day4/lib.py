

def contains(a1, a2, b1, b2):
    return a1 <= b1 and a2 >= b2


def overlaps(a1, a2, b1, b2):
    return (a1 <= b1 and b1 <= a2
            or a1 <= b2 and b2 <= a2
            or b1 <= a1 and a1 <= b2
            or b1 <= a2 and a2 <= b2)
