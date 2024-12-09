from gc import freeze
import itertools
import os
from copy import deepcopy
from pprint import pprint as pp

# from pprint import pprint as pp
# from datetime import date
from dataclassy import dataclass
from codetiming import Timer

# from dataclassy import dataclass
from icecream import ic

import utils

# YEAR and DAY from the current file name YYYY-DD.
YEAR = int(os.path.basename(__file__).split(".")[0].split("-")[0])
DAY = int(os.path.basename(__file__).split(".")[0].split("-")[1])

# Used to overwrite the year and day
# YEAR = 2015
# DAY = 07

EXAMPLE = True
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
    section_list = []
    cursor = 0
    fid = 0
    for i, length in enumerate(data):
        length = int(length)
        if length == 0:
            continue
        if i % 2 == 0:
            section_list.append(Section(start=cursor, length=length, free=False, file_index=fid))
            cursor += length
            fid += 1
        else:
            section_list.append(Section(start=cursor, length=length, free=True))
            cursor += length
    data = section_list
    return data

@dataclass
class Section():
    start: int
    length: int
    free: bool
    file_index: int = None

    @property
    def end(self):
        return self.start + self.length
    
    def __str__(self):
        return f"{self.start}: {'Free' if self.free else 'File'}{f'-{self.file_index}' if self.file_index is not None else ''} of length {self.length}"

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    for section in data:
        print(section)

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0

    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
