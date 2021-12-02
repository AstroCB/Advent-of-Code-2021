# day 2


def exec1(dirs):
    horiz = 0
    depth = 0

    for (dir, amt) in dirs:
        if dir == "forward":
            horiz += amt
        elif dir == "up":
            depth -= amt
        elif dir == "down":
            depth += amt

    return (horiz, depth)


def exec2(dirs):
    horiz = 0
    depth = 0
    aim = 0

    for (dir, amt) in dirs:
        if dir == "forward":
            horiz += amt
            depth += aim * amt
        elif dir == "up":
            aim -= amt
        elif dir == "down":
            aim += amt

    return (horiz, depth)


def run(exec_func):
    dirs = []
    with open("input.txt", "r") as f:
        lines = f.read()
        for line in filter(lambda l: l, lines.split("\n")):
            (dir, amt_str) = line.split(" ")
            dirs.append((dir, int(amt_str)))

        (horiz, depth) = exec_func(dirs)
        return horiz * depth


if __name__ == "__main__":
    print(f"part 1: {run(exec1)}")
    print(f"part 2: {run(exec2)}")