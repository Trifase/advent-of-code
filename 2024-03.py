
import os

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import itertools
from copy import deepcopy
import re



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
    data = ''.join(x for x in data)
    return data


def mul(mult_string: str) -> int:
    # mult_string should be "mul(a,b)"
    mult_string = mult_string.replace('mul', '')
    a, b = eval(mult_string)
    return a * b

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    pattern = re.compile(r"(mul\(\d*,\d*\))")
    groups = re.findall(pattern, data)

    for g in groups:
        sol1 += mul(g)

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0

    datastream = {}

    mults = re.finditer(r"(mul\(\d*,\d*\))", data)
    dos = re.finditer(r"(do\(\))", data)
    donts = re.finditer(r"(don\'t\(\))", data)

    for m in mults:
        datastream[m.start()] = m.group()
    for d in dos:
        datastream[d.start()] = True
    for d in donts:
        datastream[d.start()] = False

    # sort the dict by key
    datastream = dict(sorted(datastream.items()))

    enabled = True
    for _, v in datastream.items():
        if isinstance(v, str) and enabled:
            sol2 += mul(v)
        elif isinstance(v, bool):
            enabled = v

    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
