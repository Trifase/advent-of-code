import itertools
import os
from copy import deepcopy
from pprint import pprint as pp

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
    return data

def get_region(grid, y, x):
    """
    given a 2d matrix and a single point, return the tuple of coordinates that form the region (all adjacent points with the same values)    
    """
    r = {}
    region = set()
    region_type = grid[y][x]
    # flood fill algorithm
    points = [(y, x)]
    while points:
        # print(points)
        y, x = points.pop()
        region.add((y, x))
        neighbors = utils.get_neighbors((y, x), grid, return_dict=True)
        for coord, value in neighbors.items():
            if value == region_type and coord not in region:
                points.append(coord)
    r['points'] = region
    r['sides'] = 0
    return r

def calculate_perimeter(region, grid):
    """
    given a tuple of coords of adjacent points, calculate the perimeter of the region
    """
    perimeter = 0
    for y, x in region:
        region_type = grid[y][x]
        neighbors = utils.get_neighbors((y, x), grid, return_dict=True)
        for _, value in neighbors.items():
            if value != region_type:
                perimeter += 1
        perimeter += 4 - len(neighbors)
    return perimeter

def calculate_area(region):
    return len(region)

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    regions = []
    analyzed = set()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (y, x) not in analyzed:
                region = get_region(data, y, x)
                regions.append(region['points'])
                analyzed.update(region["points"])
    for region in regions:
        p = calculate_perimeter(region, data)
        a = calculate_area(region)
        price = p * a
        # t = next(iter(region))
        # region_type = data[t[0]][t[1]]
        # print(f"Region: {region_type} Perimeter: {p} Area: {a} Price: {price}")
        sol1 += price
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0

    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
