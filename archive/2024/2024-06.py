
import os

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import itertools
from copy import deepcopy




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
    # look for the starting point
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "^":
                guard = utils.MovingThing()
                guard.move_to((x, y))
                break
        else:
            continue
        break

    # create a set with all the edges coords:
    edges = set()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if x == 0 or y == 0 or x == len(data[y]) - 1 or y == len(data) - 1:
                edges.add((y, x))

    # add the start position to the path
    percorso = set()
    percorso.add(guard.coords)

    while guard.coords not in edges:
        a_y, a_x = guard.look_ahead
        ahead = data[a_y][a_x]
        if ahead == '#':
            guard.turn('R')
        else:
            guard.go()
            percorso.add(guard.coords)

    sol1 = len(percorso)
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    starting_pos = (0, 0)
    # we create an editable version of the grid, eg with a list of str instead of a string
    new_data = []
    for y in range(len(data)):
        new_data.append(list(data[y]))
    data = new_data

    # look for the starting point
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "^":
                starting_pos = (x, y)
                break
        else:
            continue
        break

    # create a set with all the edges coords:
    edges = set()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if x == 0 or y == 0 or x == len(data[y]) - 1 or y == len(data) - 1:
                edges.add((y, x))


    # do the first run, to see where the guard would pass as possible places to put obstacles
    guard = utils.MovingThing()
    guard.move_to(starting_pos)

    percorso_iniziale = set()

    while guard.coords not in edges:
        a_y, a_x = guard.look_ahead
        ahead = data[a_y][a_x]
        if ahead == '#':
            guard.turn('R')
        else:
            guard.go()
            percorso_iniziale.add(guard.coords)

    # create a copy of the original grid, place the guard and place an obstacle along the path, skipping the starting position
    for c in percorso_iniziale:
        y, x = c
        if (x, y) == starting_pos:
            continue

        # place the obstacle
        grid = deepcopy(data)
        grid[y][x] = '#'

        # create a new guard
        guard = utils.MovingThing()
        guard.move_to(starting_pos)

        percorso = set()
        percorso.add((guard.coords, guard.dir))
        stuck_in_loop = False

        # simula il percorso fino ad uscire o a rimanere in loop
        while guard.coords not in edges and not stuck_in_loop:

            a_y, a_x = guard.look_ahead

            ahead = grid[a_y][a_x]
            if ahead == '#':
                guard.turn('R')
            else:
                guard.go()

            # se siamo già passati da qui con la stessa direzione, siamo in un loop
            if (guard.coords, guard.dir) in percorso:
                stuck_in_loop = True
                sol2 += 1
                break
            else:
                percorso.add((guard.coords, guard.dir))

    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
