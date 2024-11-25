
from collections import defaultdict
import os
from re import A

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint

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
    We'll parse the input line by line.
    """
    return data


MAX_INT = 0xFFFF
def solve(wires, wire):
    if isinstance(wire, int) or wire.isnumeric():
        return int(wire)

    value = wires[wire]

    if isinstance(value, int) or value.isnumeric():
        return int(value)
    
    if 'AND' in value:
        a, b = value.split(' AND ')
        a = solve(wires, a)
        b = solve(wires, b)
        wires[wire] = a & b
        return a & b
    elif 'OR' in value:
        a, b = value.split(' OR ')
        a = solve(wires, a)
        b = solve(wires, b)
        wires[wire] = a | b
        return a | b
    elif 'LSHIFT' in value:
        a, b = value.split(' LSHIFT ')
        a = solve(wires, a)
        b = solve(wires, b)
        wires[wire] = (a << b) & MAX_INT
        return (a << b) & MAX_INT
    elif 'RSHIFT' in value:
        a, b = value.split(' RSHIFT ')
        a = solve(wires, a)
        b = solve(wires, b)
        wires[wire] = a >> b
        return a >> b
    elif 'NOT' in value:
        a = value.split('NOT ')[1]
        a = solve(wires, a)
        wires[wire] = MAX_INT - a
        return MAX_INT - a
    else:
        return solve(wires, value)


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    
    wires = {}
    for line in data:
        instruction, wire = line.split(' -> ')
        wires[wire] = instruction

    solve_for = 'a'
    sol1 = solve(wires, solve_for)

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    sol1 = 46065

    wires = {}
    for line in data:
        instruction, wire = line.split(' -> ')
        wires[wire] = instruction

    wires['b'] = str(sol1)

    solve_for = 'a'
    sol2 = solve(wires, solve_for)
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
