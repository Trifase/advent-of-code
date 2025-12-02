import itertools
import os
from copy import copy

from pprint import pprint as pp

from codetiming import Timer

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

    return data


def calculate_left_to_right(operation: list, wanted_result: int) -> int | None:
    result = operation[0]

    for i in range(1, len(operation), 2):
        if result > wanted_result:
            return None
        if operation[i] == "+":
            result += operation[i + 1]
        elif operation[i] == "||":
            result = int(f"{str(result)}{operation[i+1]}")
        else:
            result *= operation[i + 1]

    return result


def create_op_tree(numbers, operations):
    opt_tree = {}
    # Iterate through the numbers in pairs
    for i in range(len(numbers) - 1):
        for op in operations:
            # Create the key for the dict based on the pair and operation
            key = f"{numbers[i]}{op}{numbers[i+1]}"

            # Perform the operation
            if op == "+":
                result = numbers[i] + numbers[i + 1]
            elif op == "*":
                result = numbers[i] * numbers[i + 1]
            else:
                result = int(str(numbers[i]) + str(numbers[i + 1]))

            # Save the result to the dict
            opt_tree[key] = result
        return opt_tree


def how_many_resolve(equations: list, operations: list):
    resolved = {}
    unresolved = []
    for og_line in equations:

        line = og_line.split(": ")
        wanted_result = int(line[0])
        ops = [int(x) for x in line[1].split()]
        length = len(ops) - 1
        operations_iterations = [p for p in itertools.product(operations, repeat=length)]
        solution_found = False

        for try_ops in operations_iterations:
            numbers = copy(ops)

            for i, v in enumerate(try_ops):
                numbers.insert(2 * i + 1, v)

            result = calculate_left_to_right(numbers, wanted_result)
            if result is None:
                continue

            if result == wanted_result:
                resolved[og_line] = (wanted_result, numbers)
                solution_found = True
                break

        if not solution_found:
            unresolved.append(og_line)

    return resolved, unresolved


# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    operations = ["*", "+"]
    resolved, _ = how_many_resolve(data, operations)
    sol1 = sum(int(x[0]) for x in resolved.values())
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    operations = ["*", "+"]
    resolved, unresolved = how_many_resolve(data, operations)
    print(f"Using operators: {operations} - Resolved: {len(resolved)} - Unresolved: {len(unresolved)}")
    sol2 = sum(int(x[0]) for x in resolved.values())
    if unresolved:
        print(f"We still have unresolved: {len(unresolved)}")
        operations2 = ["*", "+", "||"]
        resolved2, unresolved2 = how_many_resolve(unresolved, operations2)
        print(f"Using operators: {operations2} - Resolved: {len(resolved2)} - Unresolved: {len(unresolved2)}")
        sol2 = sum(int(x[0]) for x in resolved2.values())
        if unresolved2:
            print(f"We still have unresolved: {len(unresolved2)}")

    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
