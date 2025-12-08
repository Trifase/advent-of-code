
import os
import time
from copy import deepcopy

from icecream import ic

import utils
from utils import MovingThing as MT

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
    return data


# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0
    grid_size_x = len(data[0])
    grid_size_y = len(data)
    grid = utils.make_grid(data)
    start_coord = (0, 0)
    for x in range(grid_size_x):
        for y in range(grid_size_y):
            if grid[y][x] == "S":
                start_coord = (x, y)
    # pprint(f"Start coord: {start_coord}")
    sol1 = resolve_tree(grid, grid_size_x, grid_size_y, start_coord, print_steps=False)
    return sol1


def cache_coord(fun):
    cache_coord.cache_ = {}
    def inner(grid, grid_size_x, grid_size_y, start_coord, count_branch, print_steps):
        if start_coord not in cache_coord.cache_:
            # print(f'Caching {id}') # to check when it is cached
            cache_coord.cache_[start_coord] = fun(grid, grid_size_x, grid_size_y, start_coord, count_branch, print_steps)
        return cache_coord.cache_[start_coord]
    return inner


def print_grid(grid, beams):
    display_grid = deepcopy(grid)

    for beam in beams:
        x, y = beam.coords_grid
        display_grid[y][x] = '|'

    for row in display_grid:
        print(''.join(row))


def resolve_tree(grid, grid_size_x, grid_size_y, start_coord, print_steps=False):
    grid = deepcopy(grid)
    # print(f"Resolving tree from {start_coord}")
    beams = []
    beam = MT()
    beam.move_to(start_coord)
    beam.turn('S')
    beams.append(beam)
    finished = False
    split_count = 0
    while not finished:
        new_beams = []
        for beam in beams:
            ahead = beam.look_ahead

            # if ahead is out of bounds, finish
            if ahead[0] < 0 or ahead[0] >= grid_size_y or ahead[1] < 0 or ahead[1] >= grid_size_x:
                finished = True
                # print(f'Reached the edge of the grid, finishing. Split count: {split_count}')
                break

            # print(f"Beam at {coord} facing {beam.dir} sees {grid[ahead[0]][ahead[1]]} ahead at {ahead}")
            
            if grid[ahead[0]][ahead[1]] == "^":

                split_count += 1
                # move the beam forward
                beam.go(1)

                # create a clone
                beam2 = MT()
                #move beam2 to the same position as beam
                beam2.move_to(beam.coords_grid)
                beam2.turn('S')

                #move beam 1 to the left
                beam.turn('L')
                beam.go(1)
                beam.turn('S')

                #move beam 2 to the right
                beam2.turn('R')
                beam2.go(1)
                beam2.turn('S')

                new_beams.append(beam)
                new_beams.append(beam2)

            else:
                beam.go(1)
                new_beams.append(beam)
        
        if not finished:
            # remove overlapping beams
            unique_coords = set()
            unique_beams = []
            for beam in new_beams:
                if beam.coords_grid not in unique_coords:
                    unique_coords.add(beam.coords_grid)
                    unique_beams.append(beam)
            beams = unique_beams

            if print_steps:
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_grid(grid, beams)
                print("==========================================")

    return split_count

@cache_coord
def resolve_tree_cache(grid, grid_size_x, grid_size_y, start_coord, count_branch=False, print_steps=False):
    grid = deepcopy(grid)
    beams = []
    beam = MT()
    beam.move_to(start_coord)
    beam.turn('S')
    beams.append(beam)
    finished = False
    split_count = 0
    while not finished:
        new_beams = []
        for beam in beams:
            ahead = beam.look_ahead

            # if ahead is out of bounds, finish
            if ahead[0] < 0 or ahead[0] >= grid_size_y or ahead[1] < 0 or ahead[1] >= grid_size_x:
                finished = True
                # print(f'Reached the edge of the grid, finishing. Split count: {split_count}')
                break

            # print(f"Beam at {coord} facing {beam.dir} sees {grid[ahead[0]][ahead[1]]} ahead at {ahead}")
            
            if grid[ahead[0]][ahead[1]] == "^":

                split_count += 1
                # move the beam forward
                beam.go(1)

                # create a clone
                beam2 = MT()
                #move beam2 to the same position as beam
                beam2.move_to(beam.coords_grid)
                beam2.turn('S')

                #move beam 1 to the left
                beam.turn('L')
                beam.go(1)
                beam.turn('S')

                #move beam 2 to the right
                beam2.turn('R')
                beam2.go(1)
                beam2.turn('S')

                if count_branch:
                    # print(f"Split at {beam.coords_grid}, duplicating paths: {beam2.coords_grid} and {beam.coords_grid}")
                    
                    dx = resolve_tree_cache(grid, grid_size_x, grid_size_y, beam2.coords_grid, count_branch=count_branch, print_steps=print_steps)
                    sx = resolve_tree_cache(grid, grid_size_x, grid_size_y, beam.coords_grid, count_branch=count_branch, print_steps=print_steps)
                    return dx + sx

                new_beams.append(beam)
                new_beams.append(beam2)

            else:
                beam.go(1)
                new_beams.append(beam)
        
        if not finished:
            # remove overlapping beams
            unique_coords = set()
            unique_beams = []
            for beam in new_beams:
                if beam.coords_grid not in unique_coords:
                    unique_coords.add(beam.coords_grid)
                    unique_beams.append(beam)
            beams = unique_beams

            if print_steps:
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_grid(grid, beams)
                print("==========================================")

    if count_branch:
        # print(f"Finished counting branches, total splits: {split_count}")
        return 1
    return split_count


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0
    grid_size_x = len(data[0])
    grid_size_y = len(data)
    grid = utils.make_grid(data)
    start_coord = (0, 0)
    for x in range(grid_size_x):
        for y in range(grid_size_y):
            if grid[y][x] == "S":
                start_coord = (x, y)
    sol2 = resolve_tree_cache(grid, grid_size_x, grid_size_y, start_coord, count_branch=True, print_steps=False)
    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
