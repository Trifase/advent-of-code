
import os

# from pprint import pprint as pp
# from datetime import date

from attr import dataclass
from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import re

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

@dataclass
class Reindeer():
    name: str
    speed: int
    fly_secs: int
    rest_sec: int

    @property
    def cycle(self):
        return self.fly_secs + self.rest_sec

    @property
    def distance_run_per_cycle(self):
        return self.speed * self.fly_secs

    def distance_at_second(self, time: int) -> int:
        cycles, rest = divmod(time, self.cycle)
        return cycles * self.distance_run_per_cycle + min(self.fly_secs, rest) * self.speed


@Timer(name="Parsing", text="Parsing.....DONE: {milliseconds:.0f} ms")
def parsing_input(data) -> any:
    """
    We'll do something with the input
    """
    reindeers = []
    for line in data:
        line = line.split()
        name, speed, fly, rest = line[0], int(line[3]), int(line[6]), int(line[13])
        reindeers.append(Reindeer(name, speed, fly, rest))
    data = reindeers
    return data


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    # ic(data)
    race = {}
    seconds = 2503

    for reindeer in data:
        km = reindeer.distance_at_second(seconds)
        race[km] = reindeer.name
        # print(f"After {seconds} seconds, {reindeer.name} has run {km} km")
    # order the dict by keys, descending
    race = dict(sorted(race.items(), key=lambda x: x[0]))
    sol1 = max(race.keys())
    print(f"The winner is {race[sol1]} with {sol1} km!")

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    points = {}
    seconds = 2503
    for sec in range(seconds):
        race = {}

        for reindeer in data:
            km = reindeer.distance_at_second(sec)
            race[km] = reindeer.name
    
        race = dict(sorted(race.items(), key=lambda x: x[0]))
        distance = max(race.keys())
        winner = race[distance]
        if winner not in points:
            points[winner] = 0
        points[winner] += 1

    # ic(points)
    # order the dict by values, descending
    points = dict(sorted(points.items(), key=lambda x: x[1]))
    winner = list(points.keys())[-1]
    print(f'The winner is {winner} with {points[winner]} points!')
    sol2 = points[winner]
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
