
import os
import itertools

from itertools import combinations
from shapely.geometry import Polygon, box

import utils

# YEAR and DAY from the current file name YYYY-DD.
YEAR = int(os.path.basename(__file__).split(".")[0].split("-")[0])
DAY = int(os.path.basename(__file__).split(".")[0].split("-")[1])

# Used to overwrite the year and day
# YEAR = 2015
# DAY = 07

EXAMPLE = False
DEBUG = True


def p(data: any) -> None:
    if DEBUG:
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
    data = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in data]
    return data



# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0
    permutations = itertools.permutations(data, 2)
    areas = set()
    for perm in permutations:
        area = (abs(perm[0][0] - perm[1][0]) + 1) * (abs(perm[0][1] - perm[1][1]) + 1)
        areas.add(area)
    sol1 = max(areas)
    return sol1


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0

    # iterate each point and connect it to the next point in the list. The last point connects to the first point. 
    # for each connections, we add the in-between points and the connection points to the perimeter
    vertices = list(data)

    polygon = Polygon(vertices)

    # Find all possible rectangles from pairs of vertices
    max_area = 0
    best_rect = None
    best_vertices = None
    checked = 0
    valid = 0

    # Check all pairs of vertices
    for i, v1 in enumerate(vertices):
        if i % 50 == 0:
            print(f"Progress: {i}/{len(vertices)} vertices checked...")
        
        for v2 in vertices[i+1:]:
            x1, y1 = v1
            x2, y2 = v2
            
            # Skip if vertices are on same horizontal or vertical line
            if x1 == x2 or y1 == y2:
                continue
            
            checked += 1
            
            # Create rectangle from these two corners
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            rect = box(min_x, min_y, max_x, max_y)
            
            # Check if rectangle is contained in polygon
            if polygon.contains(rect) or polygon.boundary.contains(rect.boundary):
                valid += 1
                area = rect.area
                if area > max_area:
                    max_area = area
                    best_rect = rect
                    best_vertices = (v1, v2)


    if best_rect:
        bounds = best_rect.bounds
        p(f'Best rectangle found: {best_vertices}')
        width = int(bounds[2] - bounds[0] + 1)
        height = int(bounds[3] - bounds[1] + 1)
        area = width * height
        sol2 = area
    return sol2



s1 = 'Not run'
s2 = 'Not run'
data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
