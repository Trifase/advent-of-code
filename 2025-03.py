
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
    data = utils.get_data(YEAR, DAY, strip=True, example=EXAMPLE)
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
    for bank in data:
        for best in range(99, -1, -1):  # range from 99 to 0
            
            first = str(best)[0]  # first number
            last = str(best)[1]  # second number
            n_first = bank.count(first)  # count of first number
            n_last = bank.count(last)  # count of last number
            if n_first == 0 or n_last == 0:  # if one of the numbers is not present
                continue  # go to next best

            i_first = [i for i, x in enumerate(bank) if x == first]  # indices of first number
            i_last = [i for i, x in enumerate(bank) if x == last]  # indices of last number
            if any(i < j for i in i_first for j in i_last):  # if any index of first is less than any index of last
                sol1 += best
                break
            # else:
                # print(f"Best {best} not found in bank {bank}")

    return sol1


# Part 2s
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0
    for bank in data:
        print(bank)
        bank = [int(x) for x in bank]
        a = 0
        b = len(bank) - 11
        max_number = []
        while len(max_number) < 12:
            # print(f"a: {a}, b: {b}")
            substring = bank[a:b]
            substring = list(substring)
            # print(f"Substring: {substring}")
            sorted_substring = sorted(substring, reverse=True)
            highest_number = sorted_substring[0]
            # print(f"Highest number: {highest_number}")
            index_highest_number = substring.index(highest_number)
            # print(f"Index highest number: {index_highest_number}")
            max_number.append(highest_number)
            a += index_highest_number + 1
            b +=1
        print(max_number)
        sol2 += int("".join([str(x) for x in max_number]))

    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
