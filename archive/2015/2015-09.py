import os

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint

import networkx as nx
from itertools import permutations

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
    G = nx.Graph()
    for line in data:
        from_, _, to, _, dist = line.split()
        G.add_edge(from_, to, weight=int(dist))

    # create a dict with all the distances between two cities
    cities_distance = {}
    for edge in G.edges:
        cities_distance[edge] = G.get_edge_data(edge[0], edge[1])['weight']
        cities_distance[edge[::-1]] = G.get_edge_data(edge[0], edge[1])['weight']
    
    # compute all the paths, save the distance and the route
    cities = list(G.nodes)
    all_routes = permutations(cities)

    distances = {}
    for route in all_routes:
        # find the distance for every route
        distance = 0
        for i in range(len(route) - 1):
            distance += cities_distance[(route[i], route[i+1])]
        distances[distance] = route

    # order distances by int(key)
    distances = dict(sorted(distances.items(), key=lambda item: item[0]))

    return distances


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    sol1 = list(data.keys())[0]
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    sol2 = list(data.keys())[-1]
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
