import os

from datetime import date
from codetiming import Timer
from icecream import ic
from rich import print

from collections import Counter

from utils import SESSIONS, get_data

# YEAR will be the current year, DAY will be the current file name.
YEAR = date.today().year
DAY = int(os.path.basename(__file__).split(".")[0])

# Used to overwrite the year and day
YEAR = 2016
# DAY = 4

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
with Timer(name="Parsing", text="Parsing.....DONE: {milliseconds:.0f} ms"):
    """
    We'll parse the input line by line.
    """
    data = get_data(YEAR, DAY, SESSIONS, strip=True, example=EXAMPLE)


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0

    for line in data:
        name, checksum = line.split("[")
        checksum = checksum[:-1]
        sector_id = int(name[-3:])
        old_name = name
        old_name = old_name[:-4]
        name = name.replace("-", "")
        name = name[:-3]

        c = Counter(name)
        c = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        c = "".join([x[0] for x in c])
        c = c[:5]
        if c == checksum:
            sol1 += sector_id
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    # data = ['qzmt-zixmtkozy-ivhz-343']
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for line in data:
        name, checksum = line.split("[")
        checksum = checksum[:-1]
        sector_id = int(name[-3:])
        name = name[:-4]
        name = name.replace("-", " ")
        c = Counter(name.replace(" ", ""))
        c = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        c = "".join([x[0] for x in c])
        c = c[:5]
        if c == checksum:
            name = list(name)
            for i, c in enumerate(name):
                if c != " ":
                    index = alphabet.index(c)
                    index += sector_id
                    index %= 26
                    name[i] = alphabet[index]
            name = ''.join(name)
            if "north" in name:
                print(name, sector_id)
                sol2 = sector_id


    return sol2


s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
