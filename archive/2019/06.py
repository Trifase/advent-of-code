import os

# from pprint import pprint as pp
from datetime import date

from codetiming import Timer
from dataclassy import dataclass
from icecream import ic
import networkx as nx
from pprint import pprint as pp

from networkx import shortest_path

from utils import SESSIONS, get_data

# YEAR will be the current year, DAY will be the current file name.
YEAR = date.today().year
DAY = int(os.path.basename(__file__).split(".")[0])

# Used to overwrite the year and day
YEAR = 2019
DAY = 6

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
with Timer(name="Parsing", text="Parsing.....DONE: {microseconds:.0f} µs"):
    """
    We'll parse the input line by line.
    """
    data: list[str] = get_data(YEAR, DAY, SESSIONS, strip=True, integers=False, example=EXAMPLE)



# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {microseconds:.0f} µs")
def part1(data: any) -> int:
    sol1 = 0
    data1 = data.copy()
    orbits = {}
    for orbit in data1:
        a, b = orbit.split(")")
        orbits[b] = a
    for planet in orbits:
        while planet in orbits:
            sol1 += 1
            planet = orbits[planet]
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {microseconds:.0f} µs")
def part2(data: any) -> int:
    sol2 = 0
    data2 = data.copy()
    start = 'YOU'
    end = 'SAN'
    orbits = {}
    for orbit in data2:
        a, b = orbit.split(")")
        if b not in orbits:
            orbits[b] = []
        orbits[b].append(a)
    # pp(orbits)
    nodes = orbits.keys()
    G = nx.Graph()
    for node in nodes:
        for parent in orbits[node]:
            G.add_edge(node, parent)

    shortestpath = nx.shortest_path(G, source=start, target=end)
    # print(shortestpath)
    sol2 = len(shortestpath) - 3
    return sol2


s1 = part1(data)
s2 = part2(data)

print()
print(f"====:: [AOC {YEAR} DAY {DAY}] ::====")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
