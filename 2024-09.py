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
    section_list = {}
    cursor = 0
    fid = 0
    for i, length in enumerate(data):
        length = int(length)
        if length == 0:
            continue
        if i % 2 == 0:
            section_list[cursor] = Section(start=cursor, length=length, free=False, file_index=fid)
            # section_list.append(Section(start=cursor, length=length, free=False, file_index=fid))
            cursor += length
            fid += 1
        else:
            section_list[cursor] = Section(start=cursor, length=length, free=True)
            # section_list.append(Section(start=cursor, length=length, free=True))
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
    
    @property
    def checksum(self):
        checksum = 0
        if self.free:
            return 0
        for i in range(self.length):
            chk = (self.start + i) * self.file_index
            checksum += chk
        return checksum
    
    def __str__(self):
        return f"{self.start}: {'Free' if self.free else 'File'}{f'-{self.file_index}' if self.file_index is not None else ''} of length {self.length}"



def move_file_in_empty_space(data, last_file_index, only_if_fits=False):
    
    if data.get(last_file_index, None):
        first_empty_space = [section for section in data.values() if section.free][0]

        available_free_space = first_empty_space.length
        last_file = data[last_file_index]
        
        if only_if_fits:
            first_empy_space = []
            first_empy_space = [section for section in data.values() if section.free and section.length >= last_file.length]
            # print(f"Trying to fit file {last_file.file_index} {last_file.start} of length {last_file.length}")
            if not first_empy_space:
                return data
            first_empty_space = first_empy_space[0]
            available_free_space = first_empty_space.length
            # print(f"Found space {first_empty_space.start} of length {first_empty_space.length}")

        if first_empty_space.start >= last_file_index:
            # print('Early return')
            return data

        # print('File space:', last_file.length, 'Empty space:', available_free_space)

        if available_free_space >= last_file.length:
            # print('It fits i guess')
            difference = available_free_space - last_file.length
            data[first_empty_space.start] = last_file
            del data[last_file.start]
            last_file.start = first_empty_space.start

            if difference != 0:
                data[first_empty_space.start + last_file.length] = Section(start=first_empty_space.start + last_file.length, length=difference, free=True)

        elif not only_if_fits:
            # print('It does not fit')
            data[first_empty_space.start] = Section(start=first_empty_space.start, length=available_free_space, free=False, file_index=last_file.file_index)
            last_file.length -= available_free_space

    data = dict(sorted(data.items()))
    return data

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0

    last_file_index = [section for section in reversed(data.values()) if not section.free][0].start
    first_space_index = [section for section in data.values() if section.free][0].start

    while last_file_index > first_space_index:
        
        print(f"Defrag: last_file_index {last_file_index} first_space_index {first_space_index}")
        data = move_file_in_empty_space(data, last_file_index)
        last_file_index = [section for section in reversed(data.values()) if not section.free][0].start
        first_space_index = [section for section in data.values() if section.free][0].start

    for section in data.values():
        if not section.free:
            sol1 += section.checksum

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0

    files = [section for section in reversed(data.values()) if not section.free]

    for file in files:
        last_file_index = file.start

        print(f"Defrag: trying to place file {last_file_index}")
        data = move_file_in_empty_space(data, last_file_index, only_if_fits=True)

    for section in data.values():
        if not section.free:
            sol2 += section.checksum

    return sol2


data = get_input()
data = parsing_input(data)
# s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
# print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
