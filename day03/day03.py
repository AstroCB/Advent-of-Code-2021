from statistics import mode


def part1(grid):
    grid_len = len(grid[0])
    # this is absolute spaghetti for the sake of a one-liner
    gamma = int("".join([mode([line[n] for line in grid]) for n in range(grid_len)]), 2)
    # drop the infinite 1s from the bitflip (two's complement makes this less pretty)
    epsilon = ~gamma & ((1 << grid_len) - 1)
    print(gamma)
    print(epsilon)
    return gamma * epsilon


with open("input.txt") as f:
    contents = f.readlines()
    grid = list(map(lambda l: [c for c in l.strip()], contents))
    print(part1(grid))