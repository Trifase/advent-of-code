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
    grid = []
    for line in data:
        grid.append(list(line))
    antennas = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != "." and data[y][x] != "#":
                antenna = data[y][x]
                if antenna not in antennas:
                    antennas[antenna] = []
                antennas[antenna].append((x, y))
    max_y, max_x = len(data), len(data[0])
    data = (grid, antennas, max_x, max_y)
    return data

def is_within_bounds(antinode, max_size):
    return 0 <= antinode[0] < max_size and 0 <= antinode[1] < max_size


def place_two_antinodes(A, B, max_size, only_one=True):

    AB_vector = (B[0] - A[0], B[1] - A[1])

    # credits to ChatGPT, a fellow math literate
    distance_AB = ((AB_vector[0])**2 + (AB_vector[1])**2)**0.5
    unit_vector = (AB_vector[0] / distance_AB, AB_vector[1] / distance_AB)

    antinodes = []

    if only_one: # return only two points, one on each side
        C = (int(B[0] + unit_vector[0] * distance_AB), int(B[1] + unit_vector[1] * distance_AB))
        D = (int(A[0] - unit_vector[0] * distance_AB), int(A[1] - unit_vector[1] * distance_AB))

        if is_within_bounds(C, max_size):
            antinodes.append(C)
        if is_within_bounds(D, max_size):
            antinodes.append(D)

    else: # return ALL THE POINTS! (Part 2)
        current_point = B
        while is_within_bounds(current_point, max_size):
            antinodes.append(current_point)
            current_point = (int(current_point[0] + unit_vector[0] * distance_AB), int(current_point[1] + unit_vector[1] * distance_AB))

        current_point = A
        while is_within_bounds(current_point, max_size):
            antinodes.append(current_point)
            current_point = (int(current_point[0] - unit_vector[0] * distance_AB), int(current_point[1] - unit_vector[1] * distance_AB))

    return antinodes


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    grid, antennas, max_x, max_y = data
    sol1 = 0
    total_antinodes = set()
    for antenna, coords in antennas.items():
        if len(coords) > 1:
            # print(f"Looking for antinodes of antenna {antenna} with points {coords}")
            permutation_coords = itertools.permutations(coords, 2)
            for A, B in permutation_coords:
                # print(f"Checking {A} and {B}")
                antinodes = place_two_antinodes(A, B, max_x)
                # print(f"Antinodes ({len(antinodes)}): {antinodes}")
                total_antinodes.update(antinodes)
    sol1 = len(total_antinodes)

    # for antinode in total_antinodes:
    #     print("Placing antinode", antinode)
    #     y, x = antinode
    #     grid[y][x] = "#"

    # for line in grid:
    #     print("".join(line))
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    grid, antennas, max_x, max_y = data
    total_antinodes = set()
    for antenna, coords in antennas.items():
        if len(coords) > 1:
            # print(f"Looking for antinodes of antenna {antenna} with points {coords}")
            permutation_coords = itertools.permutations(coords, 2)
            for A, B in permutation_coords:
                # print(f"Checking {A} and {B}")
                antinodes = place_two_antinodes(A, B, max_x, only_one=False)
                # print(f"Antinodes ({len(antinodes)}): {antinodes}")
                total_antinodes.update(antinodes)

    sol2 = len(total_antinodes)

    # for antinode in total_antinodes:
    #     print("Placing antinode", antinode)
    #     y, x = antinode
    #     grid[y][x] = "#"

    # for line in grid:
    #     print("".join(line))
    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
