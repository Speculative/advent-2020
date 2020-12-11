from math import prod, ceil


def trees_encountered(grid, right, down):
    height = len(grid)
    width = len(grid[0])
    steps = ceil(height / down)
    return sum(grid[down * step][right * step % width] == "#" for step in range(steps))


grid = [line.strip() for line in open("3.in", "r").readlines()]

# Part 1
print("Part 1:", trees_encountered(grid, 3, 1))

# Part 2
print(
    "Part 2:",
    prod(
        trees_encountered(grid, down, right)
        for down, right in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    ),
)
