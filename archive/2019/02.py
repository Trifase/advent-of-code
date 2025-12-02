import os

# from pprint import pprint as pp
from datetime import date

from codetiming import Timer
from icecream import ic

from utils import SESSIONS, get_data

# YEAR will be the current year, DAY will be the current file name.
YEAR = date.today().year
DAY = int(os.path.basename(__file__).split(".")[0])

# Used to overwrite the year and day
YEAR = 2019
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
    data: list[str] = get_data(YEAR, DAY, SESSIONS, strip=True, integers=False, example=EXAMPLE)
    data_first_line = data[0].split(",")
    data = [int(x) for x in data_first_line]


def parse_instructions(data, opcode_length): 
    for i in range(0, len(data), opcode_length):
        opcode = [int(x) for x in data[i:i+opcode_length]]
        if opcode[0] == 99:
            break
        data = parse_opcode(opcode, data)
    return data

def parse_opcode(opcode, data):
    op, a, b, pointer = opcode
    if op == 1:
        data[pointer] = data[a] + data[b]
    elif op == 2:
        data[pointer] = data[a] * data[b]
    # pprint(f'processing opcode: {opcode} - data: {data}')
    return data


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0

    data1 = data.copy()
    # replace position 1 with the value 12 and replace position 2 with the value 2
    noun = 12
    verb = 2
    data1[1] = noun
    data1[2] = verb

    data1 = parse_instructions(data1, 4)
    sol1 = data1[0]
    return sol1

# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    expected_output = 19690720
    for noun in range(100):
        for verb in range(100):
            data2 = data.copy()
            data2[1] = noun
            data2[2] = verb
            data2 = parse_instructions(data2, 4)
            if data2[0] == expected_output:
                sol2 = 100 * noun + verb
                break
        else:
            continue
        break
    return sol2


s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
