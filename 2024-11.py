import itertools
import os
from copy import deepcopy
from pprint import pprint as pp
from functools import cache

# from pprint import pprint as pp
# from datetime import date
from codetiming import Timer

# from dataclassy import dataclass
from icecream import ic

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
    data = [x for x in data[0].split()]
    return data


# remade for p2 with cache
# using strings because it's easier to split
@cache
def blink_stone(stone: str, times: int) -> int:

    if times == 0: # time for exit!
        return 1

    t1 = times -1

    # 0 stone
    if not stone or int(stone) == 0: 
        return blink_stone("1", t1)

    # even stone
    if len(stone) % 2 == 0:
        half = len(stone) // 2
        s1 = blink_stone(stone[:half], t1)
        s2 = blink_stone(stone[half:].lstrip("0"), t1)
        return s1 + s2

    # any other stone
    return blink_stone(str(int(stone) * 2024), t1)




# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    # print(data)
    for stone in data:
        sol1 += blink_stone(stone, 25)
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    for stone in data:
        sol2 += blink_stone(stone, 75)
    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
