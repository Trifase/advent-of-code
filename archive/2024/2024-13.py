# import itertools
import os
# from copy import deepcopy
# from pprint import pprint as pp

# from pprint import pprint as pp
# from datetime import date
# from codetiming import Timer

from dataclassy import dataclass
from icecream import ic

# import sympy as sp

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


@dataclass
class ClawMachine():
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]
    MAX_PRESSES: int = 100
    is_winnable = False
    a_presses = 0
    b_presses = 0
    a_token_price = 3
    b_token_price = 1
    conversion_error: bool = False

    def __post_init__(self):
        p_x, p_y = self.prize
        a_x, a_y = self.button_a
        b_x, b_y = self.button_b

        if self.conversion_error:
            error = 10000000000000
            self.prize = (p_x + error, p_y + error)
            p_x, p_y = self.prize

        # resolve linear system
        # a_x * x + b_x * y = p_x
        # a_y * x + b_y * y = p_y
        # for x and y both integers and positive

        # solution using MATHS!
        a = round((p_y - ((b_y * p_x) / b_x)) / (a_y - ((b_y * a_x) / b_x)))
        b = round((p_x - a_x * a) / b_x)
        if a_x * a + b_x * b == p_x and a_y * a + b_y * b == p_y:
            self.is_winnable = True
            self.a_presses = a
            self.b_presses = b

        # solution using sympy
        # x, y = sp.symbols('x, y')
        # eq1 = sp.Eq(a_x * x + b_x * y, p_x)
        # eq2 = sp.Eq(a_y * x + b_y * y, p_y)
        # # print(eq1, eq2)
        # ans = sp.solve((eq1, eq2), (x, y), check=False, simplify=False)
    
        # if ans[x] > 0 and isinstance(ans[x], sp.core.numbers.Integer) and ans[y] > 0 and isinstance(ans[y], sp.core.numbers.Integer):
        #     self.is_winnable = True
        #     self.a_presses = ans[x]
        #     self.b_presses = ans[y]

    def __str__(self):
        return f'ClawMachine(button_a={self.button_a}, button_b={self.button_b}, prize={self.prize})'

    @property
    def total_cost(self) -> int | None:
        return self.a_presses * self.a_token_price + self.b_presses * self.b_token_price if self.is_winnable else None


@utils.profiler(display_name="Parsing.....DONE")
def parsing_input(data) -> any:
    """
    We'll do something with the input
    """
    claws = []
    button_a: tuple[int, int] = tuple()
    button_b = tuple()
    prize = tuple()
    for line in data:
        if "Button A" in line:
            # Button A: X+94, Y+34
            dat = line.split(": ")[1]
            x, y = dat.split(", ")
            button_a = (int(x.split("+")[1]), int(y.split("+")[1]))
        elif "Button B" in line:
            # Button B: X+94, Y+34
            dat = line.split(": ")[1]
            x, y = dat.split(", ")
            button_b = (int(x.split("+")[1]), int(y.split("+")[1]))
        elif "Prize" in line:
            # Prize: X+94, Y+34
            dat = line.split(": ")[1]
            x, y = dat.split(", ")
            prize = (int(x.split("=")[1]), int(y.split("=")[1]))
        else:
            claws.append({'button_a': button_a, 'button_b': button_b, 'prize': prize})
            button_a = tuple()
            button_b = tuple()
            prize = tuple()
    # the last claw
    claws.append({'button_a': button_a, 'button_b': button_b, 'prize': prize})
    data = claws
    return data


# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0
    for claw in data:
        c = ClawMachine(button_a=claw['button_a'], button_b=claw['button_b'], prize=claw['prize'])
        if c.is_winnable and c.total_cost:
            sol1 += c.total_cost
    return sol1


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0
    for claw in data:
        c = ClawMachine(button_a=claw['button_a'], button_b=claw['button_b'], prize=claw['prize'], conversion_error=True)
        if c.is_winnable and c.total_cost:
            sol2 += c.total_cost

    return sol2


data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
