import itertools
import os
from copy import deepcopy
from pprint import pprint as pp

# from pprint import pprint as pp
# from datetime import date
from codetiming import Timer

# from dataclassy import dataclass
from icecream import ic
from regex import F

import utils

# YEAR and DAY from the current file name YYYY-DD.
YEAR = int(os.path.basename(__file__).split(".")[0].split("-")[0])
DAY = int(os.path.basename(__file__).split(".")[0].split("-")[1])

# Used to overwrite the year and day
# YEAR = 2015
# DAY = 07

EXAMPLE = False
INFO = True
DEBUG = True

if DEBUG:
    ic.enable()
else:
    ic.disable()


def pprint(data: any) -> None:
    if INFO:
        print(data)


# Input parsing
print()


@Timer(name="Opening", text="Opening.....DONE: {milliseconds:.0f} ms")
def get_input() -> any:
    """
    Get the input from the file or internet
    """
    data = utils.get_data(YEAR, DAY, strip=True, example=EXAMPLE)
    return data


@Timer(name="Parsing", text="Parsing.....DONE: {milliseconds:.0f} ms")
def parsing_input(data) -> any:
    """
    We'll do something with the input
    """
    data2 = []
    starts = set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '0':
                starts.add((y, x))
        data2.append([int(x) for x in line])
    data = (data2, starts)
    return data

def find_trails(grid, start, visited, hikes):
    next_n = start

    neighbors = utils.get_neighbors(next_n, grid)
    if not visited:
        visited = set()
    if not visited:
        hikes = []

    visited.add(start)

    starting_height = grid[start[0]][start[1]]

    if starting_height == 9:
        return
    
    for n in neighbors:
        if grid[n[0]][n[1]] - starting_height == 1:
            visited.add(n)
            if grid[n[0]][n[1]] == 9:
                hikes.append(n)
            find_trails(grid, n, visited, hikes)

    return visited, hikes

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    grid, starts = data
    for start in starts:
        score = 0

        # visited is a set of coordinates of all the cells that are part of the trail
        visited, _ = find_trails(grid, start, None, None)

        for v in visited:
            y, x = v
            if grid[y][x] == 9:
                score += 1
        print(f"Trail with start {start} has score {score}")
        sol1 += score

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    grid, starts = data
    for start in starts:
        score = 0
        # hikes is a list of coordinates of peaks, basically how many times in the trail the peak is reached
        _, hikes = find_trails(grid, start, None, None)
        score = len(hikes)
        print(f"Trail with start {start} has score {score}")
        sol2 += score

    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
