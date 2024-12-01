
import os

# from pprint import pprint as pp
# from datetime import date

from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import itertools
from copy import deepcopy



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
    replacements = []
    for line in data:
        if "=>" in line:
            key, value = line.split(" => ")
            replacements.append((key, value))
        elif line != "":
            molecule = line
    data = (replacements, molecule)
    return data

def generate_all_replacement(molecule: str, replacements: list) -> set:
    new_molecules = set()
    for key, value in replacements:
        for i in range(len(molecule)):
            if molecule[i:i+len(key)] == key:
                new_molecule = molecule[:i] + value + molecule[i+len(key):]
                new_molecules.add(new_molecule)
    return new_molecules
# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    replacements, molecule = data
    molecules = generate_all_replacement(molecule, replacements)
    sol1 = len(molecules)
    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    replacements, molecule = data
    # print(f"molecule: {molecule}")
    # print(f"replacements: {replacements}")
    step = 0
    first_step = set()
    first_step.add('e')
    while molecule not in first_step:
        # print(f'first step: {first_step}')
        step += 1
        print(f"Step: {step}")
        print(f"Initial molecules: {len(first_step)}")
        new_step = set()
        for mol in first_step:
            mols = generate_all_replacement(mol, replacements)
            # print(mols)
            for x in mols:
                new_step.add(x)
        # print(f'new step: {new_step}')
        print(f"New molecules: {len(new_step)}")
        first_step = new_step
    sol2 = step
    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")