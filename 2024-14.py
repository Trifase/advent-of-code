# import itertools
import os
# from copy import deepcopy
# from pprint import pprint as pp

# from pprint import pprint as pp
# from datetime import date
# from codetiming import Timer

from dataclassy import dataclass
from icecream import ic
from matplotlib.pyplot import grid

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
    robots = set()
    for line in data:
        #p=0,4 v=3,-3
        # print(line)
        p, v = line.split()
        p = p.replace("p=", "")
        v = v.replace("v=", "")
        x, y = p.split(",")
        x, y = int(x), int(y)
        vx, vy = v.split(",")
        vx, vy = int(vx), int(vy)
        robots.add(((x, y),(vx, vy)))
    data = robots
    return data

@dataclass
class Robot():
    x: int
    y: int
    vx: int
    vy: int

    def move(self, steps=1):
        self.x += self.vx * steps
        self.y += self.vy * steps

    def __str__(self):
        return f"Robot at ({self.y}, {self.x}), speed: {self.vy}, {self.vx})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.x, self.y, self.vx, self.vy))

    def __eq__(self, other):
        return (self.x, self.y, self.vx, self.vy) == (other.x, other.y, other.vx, other.vy)

    def __ne__(self, other):
        return not(self == other)
    
    def relative_pos(self, max_x, max_y, quadrant=False):
        # print(f"Robot at ({self.y}, {self.x})")
        # given the absolute position of the robot, translate the coordinates to the cartesian plane that has the origin in the top left corner, of x = max_x and y = max_y.
        # if the robot move outside the quadrant it wraps around.
        x = self.x % max_x
        y = self.y % max_y
        if not quadrant:
            return (y, x)
        # if quadrant is true, imagine the plane divided in 4 quadrants: 1, 2, 3, 4. The robot is in the quadrant 1 if x < max_x/2 and y < max_y/2, in the quadrant 2 if x > max_x/2 and y < max_y/2, in the quadrant 3 if x < max_x/2 and y > max_y/2, in the quadrant 4 if x > max_x/2 and y > max_y/2.
        if x < max_x//2 and y < max_y//2:
            return 1
        if x > max_x//2 and y < max_y//2:
            return 2
        if x < max_x//2 and y > max_y//2:
            return 3
        if x > max_x//2 and y > max_y//2:
            return 4
        return 0


# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0

    MAX_X, MAX_Y = 101, 103
    if EXAMPLE:
        MAX_X, MAX_Y = 11, 7

    robots = set()
    for robot in data:
        r = Robot(robot[0][0], robot[0][1], robot[1][0], robot[1][1])
        r.move(100)
        robots.add(r)

    quadrants = {}
    for robot in robots:
        q = robot.relative_pos(MAX_X, MAX_Y, quadrant=True)
        if q in quadrants:
            quadrants[q] += 1
        else:
            quadrants[q] = 1
    sol1 = quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]

    return sol1


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0

    MAX_X, MAX_Y = 101, 103
    if EXAMPLE:
        MAX_X, MAX_Y = 11, 7

    robots = set()
    for robot in data:
        r = Robot(robot[0][0], robot[0][1], robot[1][0], robot[1][1])
        robots.add(r)

    # ITERATE AND LOOK AT IT
    # for n in range(10000):
    #     rel_positions_at_100 = set()
    #     for r in robots:
    #         r.move(1)
    #         rel_pos = r.relative_pos(MAX_X, MAX_Y, quadrant=False)
    #         rel_positions_at_100.add(rel_pos)

    #     grid_prnt = [[0 for _ in range(MAX_X)] for _ in range(MAX_Y)]
    #     for y in range(MAX_Y):
    #         for x in range(MAX_X):
    #             if (y, x) in rel_positions_at_100:
    #                 grid_prnt[y][x] = "X"
    #             else:
    #                 grid_prnt[y][x] = "."

    #     for row in grid_prnt:
    #         print(''.join([str(x) for x in row]))
    #     print(f"==== [{n+1}] ====\n")

    #     # dump the content of the grid in a file, appending
    #     with open("2024-14-grids.txt", "a") as f:
    #         str_grid = '\n'.join([''.join([str(x) for x in row]) for row in grid_prnt])
    #         f.write(str_grid)
    #         f.write(f"\n==== [{n+1}] ====")
    #         f.write("\n\n")
    #     # and then STARE AT IT to find the fucking christmas tree, which, by the way, looks like this:
    #     # ...................................................X.................................................
    #     # ..................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.......X............................................
    #     # ..................X.............................X....................................................
    #     # ..........X.......X.............................X....................................................
    #     # ..................X.............................X.................X..................................
    #     # ......X...........X.............................X............................................X.......
    #     # .X................X..............X..............X....................................................
    #     # ..................X.............XXX.............X....................................................
    #     # ..................X............XXXXX............X.........X.........................X................
    #     # ....X.X...........X...........XXXXXXX...........X....................................................
    #     # .X................X..........XXXXXXXXX..........X...........X.........X..............................
    #     # ..................X............XXXXX............X..............................................X.....
    #     # ..................X...........XXXXXXX...........X.................X..................................
    #     # ..................X..........XXXXXXXXX..........X..........................X.........................
    #     # ..................X.........XXXXXXXXXXX.........X....................X...............................
    #     # ..................X........XXXXXXXXXXXXX........X....................................................
    #     # ..................X..........XXXXXXXXX..........X..........................................X...X.....
    #     # ..................X.........XXXXXXXXXXX.........X...X................................................
    #     # ..................X........XXXXXXXXXXXXX........X....................................................
    #     # ..................X.......XXXXXXXXXXXXXXX.......X..........................................X.........
    #     # ..................X......XXXXXXXXXXXXXXXXX......X....................................................
    #     # ..................X........XXXXXXXXXXXXX........X....................................................
    #     # ..................X.......XXXXXXXXXXXXXXX.......X....................................................
    #     # ..................X......XXXXXXXXXXXXXXXXX......X....X...............................................
    #     # ..................X.....XXXXXXXXXXXXXXXXXXX.....X.X...X.............X......X.........................
    #     # ..........X.......X....XXXXXXXXXXXXXXXXXXXXX....X........X...........................................
    #     # ..................X.............XXX.............X................................................X...
    #     # ..................X.............XXX.............X......................................X.............
    #     # ..................X.............XXX.............X....................................................
    #     # ..................X.............................X....................................................
    #     # ..................X.............................X............................................X.......
    #     # .X............X...X.............................X......X.............................X...............
    #     # ..................X.............................X...............X................X...................
    #     # ..................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..........X.........................................
    #     # ...........X.........................................................................................

    # added after resolution
    sol2 = 6876

    grid_prnt = [['.' for _ in range(MAX_X)] for _ in range(MAX_Y)]
    for r in robots:
        r.move(sol2)
        rel_pos = r.relative_pos(MAX_X, MAX_Y, quadrant=False)
        y, x = rel_pos
        grid_prnt[y][x] = "X"

    print(f"==== [{sol2}] ====")
    for row in grid_prnt:
        print(''.join([str(x) for x in row]))
    print(f"==== [{sol2}] ====")
    print()
        
    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
