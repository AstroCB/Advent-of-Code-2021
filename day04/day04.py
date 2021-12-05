import re
from typing import List


class Point:
    def __init__(self, point):
        x, y = point
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, start, end):
        self.start = Point(start)
        self.end = Point(end)

    # returns whether line is vertical/horizontal or not
    def is_flat(self):
        return self.start.x == self.end.x or self.start.y == self.end.y

    def leftmost(self) -> Point:
        return self.start if self.start.x < self.end.x else self.end

    def rightmost(self) -> Point:
        return self.start if self.start.x >= self.end.x else self.end

    def lowest(self) -> Point:
        return self.start if self.start.y < self.end.y else self.end

    def highest(self) -> Point:
        return self.start if self.start.y >= self.end.y else self.end

    def __str__(self):
        return f"{self.start} -> {self.end}"


class Grid:
    def __init__(self, x_max, y_max):
        self.grid = [[0 for _ in range(0, x_max + 1)] for _ in range(y_max + 1)]
        self.x_max = x_max
        self.y_max = y_max

    def mark(self, x, y):
        self.grid[y][x] += 1

    def x_range(self):
        return range(self.x_max + 1)

    def y_range(self):
        return range(self.y_max + 1)

    def is_danger(self, x, y):
        return self.grid[y][x] > 1

    def calc_danger(self):
        danger_points = 0
        for x in self.x_range():
            for y in self.y_range():
                if self.is_danger(x, y):
                    danger_points += 1
        return danger_points

    def __str__(self):
        out = ""
        for y in self.y_range():
            for x in self.x_range():
                num = self.grid[y][x]
                out += str(num) if num > 0 else "."
            out += "\n"
        return out


def part1(grid: Grid, lines: List[Line]):
    lines = filter(lambda line: line.is_flat(), lines)
    for line in lines:
        for x in range(line.leftmost().x, line.rightmost().x + 1):
            for y in range(line.lowest().y, line.highest().y + 1):
                grid.mark(x, y)
    return grid


def part2(grid: Grid, lines: List[Line]):
    # plot the vertical/horizontal lines same as before
    grid = part1(grid, lines)

    # plot diagonal lines
    lines = filter(lambda line: not line.is_flat(), lines)
    for line in lines:
        left = line.leftmost()
        right = line.rightmost()
        top = line.lowest()

        # if the left point is higher, descend L->R; otherwise, ascend
        descending = left == top

        x, y = left.x, left.y
        end_x = right.x + 1
        end_y = right.y + 1 if descending else right.y - 1

        while x != end_x or y != end_y:
            grid.mark(x, y)
            x += 1  # always moving L->R
            if left == top:
                # descends towards the lower right of the grid, towards right/bottom point
                y += 1
            else:
                # ascends towards the upper right of the grid, towards right/top point
                y -= 1
    return grid


with open("input.txt") as f:
    contents = f.readlines()
    pat = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

    lines = []
    x_max = 0
    y_max = 0
    for line in contents:
        m = pat.match(line)
        if m:
            x1 = int(m.group(1))
            y1 = int(m.group(2))
            x2 = int(m.group(3))
            y2 = int(m.group(4))

            for x in (x1, x2):
                x_max = x if x > x_max else x_max

            for y in (y1, y2):
                y_max = y if y > y_max else y_max

            lines.append(Line((x1, y1), (x2, y2)))
        else:
            print(f"failed to parse {line}")

    grid = Grid(x_max, y_max)
    print(f"Part 1: {part1(grid, lines).calc_danger()}")

    grid2 = Grid(x_max, y_max)
    print(f"Part 2: {part2(grid2, lines).calc_danger()}")
