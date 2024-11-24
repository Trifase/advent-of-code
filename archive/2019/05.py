import os

# from pprint import pprint as pp
from datetime import date

from codetiming import Timer
from dataclassy import dataclass
from icecream import ic

from utils import SESSIONS, get_data

# YEAR will be the current year, DAY will be the current file name.
YEAR = date.today().year
DAY = int(os.path.basename(__file__).split(".")[0])

# Used to overwrite the year and day
YEAR = 2019
DAY = 5

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
with Timer(name="Parsing", text="Parsing.....DONE: {microseconds:.0f} µs"):
    """
    We'll parse the input line by line.
    """
    data: list[str] = get_data(YEAR, DAY, SESSIONS, strip=True, integers=False, example=EXAMPLE)
    data_first_line = data[0].split(",")
    data = [int(x) for x in data_first_line]


@dataclass
class Opcode:
    opcode: int
    mode1: int
    mode2: int
    mode3: int
    length: int
    
    instruction_length = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        99: 0,
    }

    def __init__(self, opcode):
        opcode = str(opcode).zfill(5)  # 5 length lefpadding
        self.opcode = int(opcode[3:])
        # position = 0, immediate = 1
        self.m1 = int(opcode[2])
        self.m2 = int(opcode[1])
        self.m3 = int(opcode[0])
        self.length = self.instruction_length[self.opcode]

    def __repr__(self):
        return f"Opcode: {self.opcode} - Mode1: {self.m1} - Mode2: {self.m2} - Mode3: {self.m3} - Length: {self.length}"


def process_instruction(data, opcode, instruction, input_value):
    output_value = None
    a = 0
    b = 0
    if opcode.opcode not in [3, 4, 99]:
        a = data[instruction[1]] if opcode.m1 == 0 else instruction[1]
        b = data[instruction[2]] if opcode.m2 == 0 else instruction[2]

    if opcode.opcode == 1:
        data[instruction[3]] = a + b

    elif opcode.opcode == 2:
        data[instruction[3]] = a * b

    elif opcode.opcode == 3:
        data[instruction[1]] = input_value

    elif opcode.opcode == 4:  # outputs a new value
        output_value = data[instruction[1]]
        return data, output_value, None

    elif opcode.opcode == 5:  # returns a new cursor
        if a != 0:
            return data, None, b

    elif opcode.opcode == 6:  # returns a new cursor
        if a == 0:
            return data, None, b

    elif opcode.opcode == 7:
        data[instruction[3]] = 1 if a < b else 0

    elif opcode.opcode == 8:
        data[instruction[3]] = 1 if a == b else 0

    elif opcode.opcode == 99:  # stops
        return None, None, None

    return data, None, None  # returns the new data


def parse_data(data, cursor, input_value):
    final_output_value = None
    if not cursor:
        cursor = 0
    while data is not None:
        # print(f"Cursor: {cursor}")
        opcode = Opcode(data[cursor])
        instruction = data[cursor : cursor + opcode.length]
        # print(f"Instruction: {instruction}")
        # print(f"Opcode: {opcode}")
        cursor += opcode.length
        # print(f"Next Cursor: {cursor}")
        # print()
        data, output_value, new_cursor = process_instruction(data, opcode, instruction, input_value)
        if new_cursor is not None:  # Jump (5, 6)
            cursor = new_cursor
        if output_value is not None:  # Output (4)
            final_output_value = output_value
    return final_output_value


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {microseconds:.0f} µs")
def part1(data: any) -> int:
    sol1 = 0
    data1 = data.copy()
    input_value = 1
    sol1 = parse_data(data1, 0, input_value)
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {microseconds:.0f} µs")
def part2(data: any) -> int:
    sol2 = 0
    data2 = data.copy()
    input_value = 5
    sol2 = parse_data(data2, 0, input_value)
    return sol2


s1 = part1(data)
s2 = part2(data)

print()
print(f"====:: [AOC {YEAR} DAY {DAY}] ::====")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
