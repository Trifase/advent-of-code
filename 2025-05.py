
import os

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
    ranges = []
    ingredients = set()
    for line in data:
        if '-' in line:
            start, end = line.split('-')[0], line.split('-')[1]
            start, end = int(start), int(end)
            ranges.append((start, end))
        elif line == '':
            continue
        else:
            ingredients.add(int(line))
    data = [ranges, ingredients]
    return data


# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0
    ranges, ingredients = data
    for ingredient in ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                sol1 += 1
                break
    return sol1


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0
    ranges, _ = data

    # for each range, remove the overlap with other ranges merging the 'touching' ranges in a big range
    merged_ranges = []
    for start, end in sorted(ranges):
        if not merged_ranges or merged_ranges[-1][1] < start - 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
    ranges = merged_ranges

    for start, end in ranges:
        sol2 += end - start + 1
    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
