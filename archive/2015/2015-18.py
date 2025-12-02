
import os

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import itertools
from copy import deepcopy



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
    grid = []
    for line in data:
        grid.append([x for x in line])
    data = grid
    return data


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    this_turn = deepcopy(data)
    # print("Initial state:")
    steps = 100
    if EXAMPLE:
        steps = 5
    for step in range(steps):
        x_len = len(this_turn[0])
        y_len = len(this_turn)
        # for y in range(y_len):
        #     print("".join(this_turn[y]))
        next_turn = deepcopy(this_turn)

        for y in range(y_len):
            for x in range(x_len):
                coords = (y, x)
                this = this_turn[y][x]
                neighbors = utils.get_neighbors(coords, this_turn, diagonals=True, return_values=True)
                if this == '#':
                    if neighbors.count('#') in [2, 3]:
                        next_turn[y][x] = '#'
                    else:
                        next_turn[y][x] = '.'
                else:
                    if neighbors.count('#') == 3:
                        next_turn[y][x] = '#'
                    else:
                        next_turn[y][x] = '.'
        this_turn = deepcopy(next_turn)
        # print(f"\nAfter {step+1} steps:")
        # for y in range(y_len):
        #     print("".join(this_turn[y]))

    # Flatten the lists and count the #̀
    flat_list = list(itertools.chain(*this_turn))
    sol1 = flat_list.count('#') 
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    this_turn = deepcopy(data)


    # print("Initial state:")
    
    x_len = len(this_turn[0])
    y_len = len(this_turn)
    # Turn the corners ON
    for x, y in [(0, 0), (0, y_len-1), (x_len-1, 0), (x_len-1, y_len-1)]:
        this_turn[y][x] = '#'
    # for y in range(y_len):
    #     print("".join(this_turn[y]))
    steps = 100
    if EXAMPLE:
        steps = 5
    for step in range(steps):
        x_len = len(this_turn[0])
        y_len = len(this_turn)
        next_turn = deepcopy(this_turn)

        for y in range(y_len):
            for x in range(x_len):
                coords = (y, x)
                this = this_turn[y][x]
                neighbors = utils.get_neighbors(coords, this_turn, diagonals=True, return_values=True)
                if this == '#':
                    if neighbors.count('#') in [2, 3]:
                        next_turn[y][x] = '#'
                    else:
                        next_turn[y][x] = '.'
                else:
                    if neighbors.count('#') == 3:
                        next_turn[y][x] = '#'
                    else:
                        next_turn[y][x] = '.'

        # Turn the corners ON
        for x, y in [(0, 0), (0, y_len-1), (x_len-1, 0), (x_len-1, y_len-1)]:
            next_turn[y][x] = '#'

        this_turn = deepcopy(next_turn)
        # print(f"\nAfter {step+1} steps:")
        # for y in range(y_len):
        #     print("".join(this_turn[y]))

    # Flatten the lists and count the #̀
    flat_list = list(itertools.chain(*this_turn))
    sol2 = flat_list.count('#') 
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
