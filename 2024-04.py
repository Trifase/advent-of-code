
import os

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import itertools
from copy import deepcopy

from matplotlib import use



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
    return data


def get_possible_words(grid, x, y, length=4):
    """
    given a lists of list, find the next 3 neightboor in every direction (diagonals included) and return their value
    
    3..3..3
    .2.2.2.
    ..111..
    321X123
    ..111..
    .2.2.2.
    3..3..3
    """
    directions = {
        (0, -1) : '↑',  # up
        (0, 1) : '↓',   # down
        (-1, 0) : '←',  # left
        (1, 0) : '→',   # right
        (1, -1) : '↗', # top-right
        (1, 1) : '↘',   # bottom-right
        (-1, 1) : '↙',  # bottom-left
        (-1, -1) : '↖', # top-left
    }
    
    words = {}

    for dx, dy in directions.keys():
        direction_values = []
        for step in range(length):
            nx, ny = x + dx * step, y + dy * step
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                direction_values.append(grid[ny][nx])
            else:
                break
        words[directions[(dx, dy)]] = direction_values

    return words

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "X":
                words = get_possible_words(data, x, y)
                p = len([x for x in words.values() if ''.join(x) == 'XMAS'])

                sol1 += p

    return sol1

def is_xmas(words):
    """
    given the value of the 8 neighbors of a cell, checks if the word MAS is in the 4 diagonal directions, in pairs

    | M.M | S.M | M.S | S.S |
    | .A. | .A. | .A. | .A. |
    | S.S | S.M | M.S | M.M |

    the list is ordered as follows:

    7 0 4
    3 X 1
    6 2 5

    0, 1, 2, 3 will be ignored
    """
    xmas = False
    _, _, _, _, tr, br, bl, tl = words
    if tr == tl == 'M' and br == bl == 'S':
        xmas = True
    if tr == br == 'M' and tl == bl == 'S':
        xmas = True
    if tr == br == 'S' and tl == bl == 'M':
        xmas = True
    if tr == tl == 'S' and br == bl == 'M':
        xmas = True
    return xmas


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "A":
                words = utils.get_neighbors((y, x), data, diagonals=True, return_values=True)
                if len(words) == 8 and is_xmas(words):
                    sol2 += 1

    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
