
import os

# from pprint import pprint as pp
# from datetime import date

from attr import dataclass
from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import itertools


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

def find_subsets_that_sum_to_target(nums, target):
    valid_subsets = []

    for r in range(1, len(nums) + 1):
        for subset in itertools.combinations(nums, r):
            if sum(subset) == target:
                valid_subsets.append(subset)

    return valid_subsets


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
    data = [int(x) for x in data]
    target =150
    if EXAMPLE:
        target = 25

    valid_subsets = find_subsets_that_sum_to_target(data, target)
    data = valid_subsets
    return data


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0

    sol1 = len(data)
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    last_len = 5000  # arbitrary large
    for subset in data:
        if len(subset) < last_len:
            sol2 = 1
            last_len = len(subset)
        elif len(subset) == last_len:
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
