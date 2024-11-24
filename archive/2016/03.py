from codetiming import Timer
from icecream import ic
from rich import print

from utils import SESSIONS, get_data

YEAR = 2016
DAY = 3

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
        a, b, c = [int(x) for x in line.split()]
        if a + b > c and a + c > b and b + c > a:
            sol1 += 1

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    for i in range(0, len(data), 3):
        a1, b1, c1 = [int(x) for x in data[i].split()]
        a2, b2, c2 = [int(x) for x in data[i + 1].split()]
        a3, b3, c3 = [int(x) for x in data[i + 2].split()]
        if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
            sol2 += 1
        if b1 + b2 > b3 and b1 + b3 > b2 and b2 + b3 > b1:
            sol2 += 1
        if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
            sol2 += 1

    return sol2


s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
