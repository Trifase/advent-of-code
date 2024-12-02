
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
    d2 = []
    for line in data:
        d2.append([int(x) for x in line.split()])
    data = d2
    return data

def is_safe(line: list):
    safe = True
    order = ''

    if line[1] > line[0]: 
        order = 'asc'

    for i in range(len(line) - 1):
        a, b = line[i], line[i + 1]

        # check for distance
        if abs(a - b) > 3 or abs(a - b) < 1:
            safe = False
            break

        # check for order
        if order == 'asc':
            if a > b:
                safe = False
                break
        else:
            if a < b:
                safe = False
                break

    return safe


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    sol1 = sum([1 for x in data if is_safe(x)])
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    safe = []
    unsafe = []

    for x in data:
        if is_safe(x):
            safe.append(x)
        else:
            unsafe.append(x)

    # trying to fix the unsafe lines, removing one item at a time
    for x in unsafe:
        resolved = False

        for i in range(len(x)):
            if resolved:
                continue

            line2: list = deepcopy(x)
            line2.pop(i)

            if is_safe(line2):
                safe.append(line2)
                resolved = True
                break

    sol2 = len(safe)
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
