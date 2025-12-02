
import os

# from pprint import pprint as pp
# from datetime import date

from attr import dataclass
from codetiming import Timer
# from dataclassy import dataclass
from icecream import ic
from pprint import pprint as pp
import itertools


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


@dataclass(frozen=True)
class Ingredient():
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


@dataclass
class Cookie():
    name: str
    ingredients: dict   # ingredients example: {Ingredient1: 44, Ingredient2: 56}

    @property
    def score(self):
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0

        for k, v in self.ingredients.items():
            capacity += v * k.capacity
            durability += v * k.durability
            flavor += v * k.flavor
            texture += v * k.texture
            calories += v * k.calories

        if capacity < 0:
            capacity = 0
        if durability < 0:
            durability = 0
        if flavor < 0:
            flavor = 0
        if texture < 0:
            texture = 0

        score = capacity * durability * flavor * texture
        return score

    @property
    def cal(self):
        calories = 0

        for k, v in self.ingredients.items():
            calories += v * k.calories

        return calories


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
    ingredients = []

    for line in data:
        ing = {}
        name = line.split(":")[0]
        for i in line.split(":")[1].split(","):
            ing[i.split()[0]] = int(i.split()[1])
        ingredients.append(Ingredient(name, **ing))

    data = ingredients
    print('Total ingredients: ', len(data))

    permutations = generate_permutations(data, 100)
    print(f'Permutations: {len(permutations)}')

    return (data, permutations)

def generate_permutations(ingredients, total_ingredients):
    print('Generating permutations')
    permutations = []
    for distribution in itertools.product(range(1, total_ingredients), repeat=len(ingredients)):
        if sum(distribution) == total_ingredients:
            permutation = dict(zip(ingredients, distribution))
            permutations.append(permutation)
    
    return permutations

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    best_recipe = {}
    data, permutations = data

    for i, perm in enumerate(permutations):
        cookie = Cookie(name=f'Biscotto {i}', ingredients=perm)

        if cookie.score > sol1:
            best_recipe = perm
            sol1 = cookie.score

    print('\nBest recipe:')
    for k, v in best_recipe.items():
        print(f'{k.name}: {v}')

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    best_recipe = {}
    MAX_CAL = 500
    data, permutations = data

    for i, perm in enumerate(permutations):
        cookie = Cookie(name=f'Biscotto {i}', ingredients=perm)

        if cookie.cal == MAX_CAL and cookie.score > sol2:
            best_recipe = perm
            sol2 = cookie.score

    print(f'\nBest recipe ({MAX_CAL} calories):')
    for k, v in best_recipe.items():
        print(f'{k.name}: {v}')

    return sol2

data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
