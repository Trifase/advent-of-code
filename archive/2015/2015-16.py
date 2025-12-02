
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
    aunts = []
    for line in data:
        aunt = {}
        line = line.replace(":", "").replace(",", "").split()
        aunt["number"] = int(line[1])
        for i in range(2, len(line), 2):
            aunt[line[i]] = int(line[i+1])
        aunts.append(aunt)
    data = aunts
    return data


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    aunt_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    for aunt in data:
        keys = list(aunt.keys())
        keys.remove("number")
        if all(aunt[key] == aunt_sue[key] for key in keys):
            sol1 = aunt["number"]
            break
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    aunt_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    for aunt in data:
        keys = 0
        for key in aunt:
            if key == "number":
                continue
            if key in ["cats", "trees"]:
                if aunt[key] > aunt_sue[key]:
                    keys += 1
            elif key in ["pomeranians", "goldfish"]:
                if aunt[key] < aunt_sue[key]:
                    keys += 1
            else:
                if aunt[key] == aunt_sue[key]:
                    keys += 1

        if keys == len(aunt) - 1:  # gotta exclude 'number'
            sol2 = aunt["number"]
            break
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
