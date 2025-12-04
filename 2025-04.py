
import os
from copy import deepcopy

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
    data = utils.make_grid(data)
    # print(data)
    return data


# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            coords = (y, x)
            this = data[y][x]
            if this == '@':
                neighbors = utils.get_neighbors(coords, data, diagonals=True, return_values=True)

                if neighbors.count('@') < 4:
                    sol1 += 1
    return sol1


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0
    this_turn = data
    continue_loop = True
    while continue_loop:
        deleted_this_turn = []
        x_len = len(this_turn[0])
        y_len = len(this_turn)

        for y in range(y_len):
            for x in range(x_len):
                coords = (y, x)
                this_cell = this_turn[y][x]
                if this_cell == '@':
                    neighbors = utils.get_neighbors(coords, this_turn, diagonals=True, return_values=True)  # get neighbors for this cell
                    if neighbors.count('@') < 4:
                        sol2 += 1
                        deleted_this_turn.append(coords)

        if not deleted_this_turn:  # no more to delete
            continue_loop = False  # unecessary but explicit
            break

        else:
            next_turn = deepcopy(this_turn)  # this will be the next iteration
            for coord in deleted_this_turn:
                y, x = coord
                next_turn[y][x] = '.'  # replace paper with empty space

        this_turn = next_turn
        deleted_this_turn = []


    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
