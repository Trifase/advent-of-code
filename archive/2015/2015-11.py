from operator import is_
import os

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pp
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


@Timer(name="Parsing", text="Parsing.....DONE: {milliseconds:.0f} ms")
def parsing_input(data) -> any:
    """
    We'll do something with the input
    """
    data = data[0]
    return data

# Create a generator that given a string 'abc', iterate the next string 'abd, abe, abf, ...abz → aca, acb, ...azz → baa, bab, ... zzz'
def next_string(s: str) -> str:
    """
    Given a string 'abc', iterate the next string 'abd, abe, abf, ...abz → aca, acb, ...azz → baa, bab, ... zzz'
    Skip i, o, l
    """
    s = list(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'z':
            s[i] = 'a'
        # skipping i, o, l 
        elif s[i] in "hnk":
            s[i] = chr(ord(s[i]) + 2)
            break
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    return "".join(s)

# RULES:

# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
def rule1(s: str) -> bool:
    """
    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    """
    return not any(c in s for c in "iol")

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
def rule2(s: str) -> bool:
    """
    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    """
    for i in range(len(s) - 2):
        if ord(s[i]) == ord(s[i + 1]) - 1 == ord(s[i + 2]) - 2:
            return True
    return False


# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
def rule3(s: str) -> bool:
    """
    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    """
    pairs = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs >= 2


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    found = False
    password = 'cqjxjnds'
    # i = 0
    while not found:
        # if i % 1000 == 0:
        #     print(password, end=" ")
        password = next_string(password)
        # if i % 1000 == 0:
        #     print(f"→ {password}")
        # i += 1
        if rule1(password) and rule2(password) and rule3(password):
            found = True
            sol1 = password
            break

    # print(password)

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0

    found = False
    password = 'cqjxxyzz'
    # i = 0
    while not found:
        # if i % 1000 == 0:
            # print(f"[{i}] {password}", end=" ")
        password = next_string(password)
        # if i % 1000 == 0:
            # print(f"→ {password}")
        # i += 1
        if rule1(password) and rule2(password) and rule3(password):
            found = True
            sol2 = password
            break

    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
