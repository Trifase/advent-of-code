
import os

from dataclassy import dataclass
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


@utils.profiler(display_name="Opening.....DONE")
def get_input() -> any:
    """
    Get the input from the file or internet
    """
    data = utils.get_data(YEAR, DAY, strip=True, example=EXAMPLE)
    return data


@utils.profiler(display_name="Parsing.....DONE")
def parsing_input(data) -> any:
    """
    We'll do something with the input
    """
    data = data[0].split(",")
    
    # print(data)
    return data


# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0
    for _range in data:
        start, end = map(int, _range.split("-"))
        for n in range(start, end + 1):
            n = str(n)
            ln = len(n)
            # only for even length numbers
            if ln % 2 == 0:
                half_len = ln // 2
                first_half = n[:half_len]
                second_half = n[half_len:]
                if first_half == second_half:
                    sol1 += int(n)

    return sol1


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0
    for _range in data:
            start, end = map(int, _range.split("-"))
            for n in range(start, end + 1):
                n = str(n)
                ln = len(n)
                # list of divisors of ln
                divisors = [i for i in range(1, ln + 1) if ln % i == 0]
                # remove 1 from the divisors
                divisors = [d for d in divisors if d != 1]

                for d in divisors:
                    part_len = ln // d
                    parts = [n[i * part_len:(i + 1) * part_len] for i in range(d)]
                    if all(part == parts[0] for part in parts):
                        # print(f"n: {n}, is made of {parts[0]} * {d} times")
                        sol2 += int(n)
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
