def up_score(grid, i, j):
    height = grid[i][j]
    s = 0
    while i-1 >= 0:
        i = i-1
        s += 1
        if grid[i][j] >= height:
            break
    return s


def down_score(grid, i, j):
    height = grid[i][j]
    s = 0
    while i+1 < len(grid):
        i = i+1
        s += 1
        if grid[i][j] >= height:
            break
    return s


def right_score(grid, i, j):
    height = grid[i][j]
    s = 0
    while j+1 < len(grid[0]):
        j = j+1
        s += 1
        if grid[i][j] >= height:
            break
    return s


def left_score(grid, i, j):
    height = grid[i][j]
    s = 0
    while j-1 >= 0:
        j = j-1
        s += 1
        if grid[i][j] >= height:
            break
    return s


def score(grid, i, j):
    up = up_score(grid, i, j)
    left = left_score(grid, i, j)
    right = right_score(grid, i, j)
    down = down_score(grid, i, j)
    print(f"{up}, {left}, {right}, {down}")
    return up * left * right * down
