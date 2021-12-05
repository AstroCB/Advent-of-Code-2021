from statistics import mode


def part1(grid):
    grid_len = len(grid[0])
    # this is absolute spaghetti for the sake of a one-liner
    gamma = int("".join([mode([line[n] for line in grid]) for n in range(grid_len)]), 2)
    # drop the infinite 1s from the bitflip (two's complement makes this less pretty)
    epsilon = ~gamma & ((1 << grid_len) - 1)
    return gamma * epsilon


def calc(grid, filter_criteria):
    numbers = [line for line in grid]
    for n in range(len(grid[0])):
        numbers = filter_criteria(numbers, n)
        if len(numbers) == 1:
            return "".join(numbers[0])


def oxygen(numbers, n):
    col = [num[n] for num in numbers]
    val = "1" if col.count("1") >= col.count("0") else "0"
    return list(filter(lambda num: num[n] == val, numbers))


def co2(numbers, n):
    col = [num[n] for num in numbers]
    val = "1" if col.count("0") > col.count("1") else "0"
    return list(filter(lambda num: num[n] == val, numbers))


def part2(grid):
    ox_gen = int(calc(grid, oxygen), 2)
    co2_scrub = int(calc(grid, co2), 2)
    return ox_gen * co2_scrub


with open("input.txt") as f:
    contents = f.readlines()
    grid = list(map(lambda l: [c for c in l.strip()], contents))
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")