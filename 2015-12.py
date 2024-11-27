
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
    return data


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0

    sol1 = sum([int(x) for x in re.findall('-?[0-9]+', data[0])])
    return sol1

def return_number(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum([return_number(x) for x in data if not isinstance(x, str)])
    
    elif isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum([return_number(x) for x in data.values() if not isinstance(x, str)])
    
# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    data = eval(data[0])
    # data = ['[1,2,3]', '[1,{"c":"red","b":2},3]', '{"d":"red","e":[1,2,3,4],"f":5}', '[1,"red",5]']
    # for d in data[:4]:
    #     c = eval(d)
    #     print(f"{d} → {return_number(c)}")
    sol2 = return_number(data)
    return sol2

data = get_input()
data = parsing_input(data)
# s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
# print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
