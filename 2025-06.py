
import os

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


@utils.profiler(display_name="Opening.....DONE")
def get_input() -> any:
    """
    Get the input from the file or internet
    """
    data = utils.get_data(YEAR, DAY, strip=False, example=EXAMPLE)
    return data


@utils.profiler(display_name="Parsing.....DONE")
def parsing_input(data) -> any:
    """
    We'll do something with the input
    """
    return data


# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0
    problems = {}
    for line in data:
        for x, n in enumerate(line.split()):
            if x not in problems:
                problems[x] = []
            problems[x].append(n)
            
    for p in problems.values():
        op = p[-1]
        prob = f"{op.join(p[:-1])}"
        # print(f"Problem: {prob}")
        sol1 += eval(prob)
    return sol1


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0
    
    problems = {}
    # # we need to mantaing spacing and whitespaces, so we need to understand the column width:
    # length = 0
    # for i in range(len(data[-1])):
    #     if all(r[i] == " " for r in data):
    #         length = i
    #         break
    # lenghts are variable
    lengths = []
    for i in range(len(data[-1])):
        if all(r[i] == " " for r in data):
            lengths.append(i)
    # print(f"Length: {length}")

    for line in data:
        cur = 0
        for x in range(len(lengths)+1):
            if x == 0:
                chunk = line[0:lengths[0]]
                cur = lengths[0]
            elif x == len(lengths):
                chunk = line[cur:]
            else:
                chunk = line[cur:lengths[x]]
                cur = lengths[x]
            if x not in problems:
                problems[x] = []
            problems[x].append(chunk)


    # So for example p is: ['123', ' 45', '  6', '*  ']
    # the original column was:
    # 123
    #  45
    #   6
      
    # we look at the number as it were colums, so 1 24 356

    # basically we need to rotate the numbers ccw
    for p in problems.values():
        op = p[-1].strip()
        # rotate ccw
        rotated = []
        max_len = max(len(r) for r in p[:-1])
        for i in range(max_len):
            new_row = ""
            for r in (p[:-1]):
                if i < len(r):
                    new_row += r[i]
                else:
                    new_row += " "
            rotated.append(new_row.rstrip())
        # now we have the rotated numbers
        numbers = [r.strip() for r in rotated if r.strip() != ""]
        op = f" {op} "
        prob = f"{op.join(numbers).strip()}"
        # print(f"Problem: {prob} = {eval(prob)}")
        sol2 += eval(prob)

      
    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
