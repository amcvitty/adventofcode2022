
def any_score(grid, i, j, fn):
    "The function passed as the last arg is the traversal"
    height = grid[i][j]
    visible_trees = 0
    i, j = fn(i, j)
    # while we're still on the grid, traverse
    while i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
        visible_trees += 1
        # Stop if this is the last tree
        if grid[i][j] >= height:
            break
        i, j = fn(i, j)

    return visible_trees


def up_score(grid, i, j):
    def go_up(i, j): return i-1, j
    return any_score(grid, i, j, go_up)


def down_score(grid, i, j):
    def go_down(i, j): return i+1, j
    return any_score(grid, i, j, go_down)


def right_score(grid, i, j):
    def go_down(i, j): return i, j+1
    return any_score(grid, i, j, go_down)


def left_score(grid, i, j):
    def go_down(i, j): return i, j-1
    return any_score(grid, i, j, go_down)


def score(grid, i, j):
    up = up_score(grid, i, j)
    left = left_score(grid, i, j)
    right = right_score(grid, i, j)
    down = down_score(grid, i, j)
    print(f"{up}, {left}, {right}, {down}")
    return up * left * right * down
