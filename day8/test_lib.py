from lib import *


def test_one():
    with open("example.txt") as f:
        lines = f.readlines()
        grid = [[int(d) for d in line.strip()] for line in lines]

    assert up_score(grid, 0, 0) == 0
    assert up_score(grid, 2, 0) == 2
    assert up_score(grid, 3, 0) == 1

    assert down_score(grid, 0, 3) == 4
    assert score(grid, 1, 2) == 4
    assert score(grid, 3, 2) == 8
