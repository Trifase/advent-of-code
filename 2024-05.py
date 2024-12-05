
from functools import total_ordering
import os
from re import A

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
    split_i = data.index("")
    
    rules = data[:split_i]
    rules = [(a, b) for a, b in [x.split('|') for x in rules]]
    
    updates = data[split_i+1:]
    updates = [[int(x) for x in update.split(',')] for update in updates]

    data = rules, updates

    return data

def get_enabled_rules(rules, update):
    enabled_rules = []
    for rule in rules:
        a, b = rule
        if all([int(x) in update for x in [a, b]]):
            enabled_rules.append(rule)
    return enabled_rules

def is_update_correct(enabled_rules, update):
    for rule in enabled_rules:
        a, b = rule
        if update.index(int(a)) > update.index(int(b)):
            return False
    return True

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    rules, updates = data
    for update in updates:
        enabled_rules = get_enabled_rules(rules, update)
        if is_update_correct(enabled_rules, update):
            sol1 += update[len(update)//2]
    return sol1

def try_sort(update, rule):
    a, b = rule
    a_index = update.index(int(a))
    b_index = update.index(int(b))
    update.insert(a_index, update.pop(b_index))
    return update

# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    rules, updates = data

    for update in updates:
        enabled_rules = get_enabled_rules(rules, update)

        if not is_update_correct(enabled_rules, update):
            # we try to fix it
            while not is_update_correct(enabled_rules, update):
                for rule in enabled_rules:
                    a, b = rule
                    if update.index(int(a)) > update.index(int(b)):
                        update = try_sort(update, rule)

            sol2 += update[len(update)//2]
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
