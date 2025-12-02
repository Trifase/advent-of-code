from codetiming import Timer
from icecream import ic

# from rich import print
from utils import SESSIONS, MovingThing, get_data

# from PIL import Image

YEAR = 2016
DAY = 1

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
    data = [x.strip() for x in data[0].split(", ")]


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0

    me = MovingThing()
    # print(me.coords)

    for m in data:
        rotation = m[0]
        steps = int(m[1:])
        me.turn(rotation)
        me.go(steps)
        # print(me.coords)

    sol1 = sum(abs(x) for x in me.coords)
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0

    me2 = MovingThing()
    locs = []
    # offset = 100
    # img = Image.new('RGB', (500, 500))

    for m in data:
        found = False
        rotation = m[0]
        steps = int(m[1:])
        me2.turn(rotation)
        print(f"Going {rotation}, and then {steps} steps - dir: {me2.dir}")
        for _ in range(steps):
            # i = int(255/steps)
            me2.go(1)
            print(me2.coords)
            # x = (me2.coords[0] + offset, me2.coords[1] + offset)
            # img.putpixel(x, (250, 250 - i, 0 + i))
            if me2.coords in locs:
                print("Alt! Ho già visitato questo posto!")
                sol2 = sum(abs(x) for x in me2.coords)
                found = True
                break
            else:
                locs.append(me2.coords)
        # img.save('sqr.png')
        if found:
            break
        print()

    return sol2


s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
