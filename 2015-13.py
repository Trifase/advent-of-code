
import os

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import re

import networkx as nx
from itertools import permutations

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
    happiness = {}
    for line in data:
        line = line.replace(".", "").split()
        one, action, value, who = line[0], line[2], int(line[3]), line[-1]
        if action == "lose":
            value = -value
        if one not in happiness:
            happiness[one] = {}
        happiness[one][who] = value
    data = happiness
    return data


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    happinessess = {}
    for perm in permutations(data.keys()):
        total = 0
        for i in range(len(perm)):
            total += data[perm[i]][perm[i-1]] + data[perm[i]][perm[(i+1) % len(perm)]]
        happinessess[total] = perm
    #reorder the dict by key value
    happinessess = dict(sorted(happinessess.items(), key=lambda x: x[0]))
    sol1 = max(happinessess.keys())
    pp(f"Best arrangement: {sol1} → {happinessess[sol1]}")
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    sol1 = 618
    data["Luca"] = {}
    for key in data.keys():
        data[key]["Luca"] = 0
        data["Luca"][key] = 0
    # pp(data)
    happinessess = {}
    for perm in permutations(data.keys()):
        total = 0
        for i in range(len(perm)):
            total += data[perm[i]][perm[i-1]] + data[perm[i]][perm[(i+1) % len(perm)]]
        happinessess[total] = perm
    #reorder the dict by key value
    happinessess = dict(sorted(happinessess.items(), key=lambda x: x[0]))
    # ic(happinessess)
    sol2 = max(happinessess.keys())
    pp(f"Best arrangement: {sol2} → {happinessess[sol2]}")
    sol2 = abs(sol2 - sol1)
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
