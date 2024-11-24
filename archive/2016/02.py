from codetiming import Timer
from icecream import ic
from rich import print

from utils import SESSIONS, MovingThing, get_data

YEAR = 2016
DAY = 2

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
    sol1 = ""

    finger = MovingThing()

    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    finger.move_to((1, 1))

    for line in data:
        for c in line:
            finger.grid_move(c)
            if finger.y < 0:
                finger.y = 0
            if finger.y > 2:
                finger.y = 2
            if finger.x < 0:
                finger.x = 0
            if finger.x > 2:
                finger.x = 2
        sol1 += str(pad[finger.y][finger.x])

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    sol2 = ""

    finger = MovingThing()

    pad = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, "A", "B", "C", 0],
        [0, 0, "D", 0, 0],
    ]

    finger.move_to((0, 2))

    for line in data:
        for c in line:
            old_pos = finger.coords
            finger.grid_move(c)
            if finger.y < 0:
                finger.y = 0
            if finger.y > 4:
                finger.y = 4
            if finger.x < 0:
                finger.x = 0
            if finger.x > 4:
                finger.x = 4
            if pad[finger.y][finger.x] == 0:
                finger.coords = old_pos
        sol2 += str(pad[finger.y][finger.x])

    return sol2


s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
