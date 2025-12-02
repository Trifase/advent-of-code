import os

# from pprint import pprint as pp
from datetime import date

from codetiming import Timer
from icecream import ic
from dataclassy import dataclass

from utils import SESSIONS, get_data

# YEAR will be the current year, DAY will be the current file name.
YEAR = date.today().year
DAY = int(os.path.basename(__file__).split(".")[0])

# Used to overwrite the year and day
# YEAR = 2016
# DAY = 4

EXAMPLE = True
INFO = True
DEBUG = True

if DEBUG:
    ic.enable()
else:
    ic.disable()


def pprint(data: any) -> None:
    if INFO:
        print(data)

@dataclass
class Part():
    x = 0
    m = 0
    a = 0
    s = 0

    def __repr__(self):
        return f"Part(x={self.x}, m={self.m}, a={self.a}, s={self.s})"
    
    def __str__(self):
        return f"Part(x={self.x}, m={self.m}, a={self.a}, s={self.s})"

class Rule():
    name = ''
    conditions = []
    destination = ''

    def __repr__(self):
        return f"Rule(name={self.name}, conditions={self.conditions}, destination={self.destination})"

    def __str__(self):
        return f"Rule(name={self.name}, conditions={self.conditions}, destination={self.destination})"

# Input parsing
print()
with Timer(name="Parsing", text="Parsing.....DONE: {milliseconds:.0f} ms"):
    """
    We'll parse the input line by line.
    """
    data = get_data(YEAR, DAY, SESSIONS, strip=True, example=EXAMPLE)

    rules = []
    parts = []

    parts_parsing = False
    for line in data:
        if line == '':
            parts_parsing = True
            continue

        if parts_parsing:
            part = Part()
            line = line[1:-1].split(',')
            for prop in line:
                prop = prop.split('=')
                if prop[0] == 'x':
                    part.x = int(prop[1])
                if prop[0] == 'm':
                    part.m = int(prop[1])
                if prop[0] == 'a':
                    part.a = int(prop[1])
                if prop[0] == 's':
                    part.s = int(prop[1])

            parts.append(part)

        else:
            rule = Rule()
            conds = []
            name, conditions = line.split('{')
            rule.name = name.strip()
            conditions = conditions[:-1].split(',')
            rule.destination = conditions.pop().strip()

            for cond in conditions:
                cond = cond.split(':')
                dest = cond[-1].strip()
                check = cond[0][0]
                comp = cond[0][1]
                value = int(cond[0][2:])
                conds.append((check, comp, value, dest))
            rule.conditions = conds
            rules.append(rule)

    data = (rules, parts)


def find_rule_by_name(rules: list, name: str) -> Rule:
    for rule in rules:
        if rule.name == name:
            return rule
    return None

def check_part_against_condition(condition: tuple, part: Part) -> bool:
    check, comp, value, dest = condition
    match check:
        case 'x':
            if comp == '<':
                return part.x < value
            else:
                return part.x > value
        case 'm':
            if comp == '<':
                return part.m < value
            else:
                return part.m > value
        case 'a':
            if comp == '<':
                return part.a < value
            else:
                return part.a > value
        case 's':
            if comp == '<':
                return part.s < value
            else:
                return part.s > value



def analyze_part(rules: list, part: Part, rule_name: str = None) -> str:
    if not rule_name:
        rule_name = 'in'
    # print(f"Analyzing part {part} with rule {rule_name}")
    rule = find_rule_by_name(rules, rule_name)
    for condition in rule.conditions:
        # print(f"Checking condition {condition}")
        result = check_part_against_condition(condition, part)
        # print(f"Result: {result}")
        if result:
            destination = condition[-1]
            # print(f"Destination: {destination}")
            if destination == 'A':
                # print("Part is accepted")
                return 'A'
            elif destination == 'R':
                # print("Part is refused")
                return 'R'
            else:
                # print(f" will analize part {part} with rule {destination}")
                return analyze_part(rules, part, destination)

    # print(f'No condition matched, going {rule.destination}')
    if rule.destination == 'A':
        # print("Part is accepted")
        return 'A'
    elif rule.destination == 'R':
        # print("Part is refused")
        return 'R'
    else:
        # print(f" will analize part {part} with rule {rule.destination}")
        return analyze_part(rules, part, rule.destination)

# Part 1
@Timer(name="Part 1", text="Part 1......DONE: {milliseconds:.0f} ms")
def part1(data: any) -> int:
    sol1 = 0
    # print(data)
    rules, parts = data
    rule_name = 'in'

    accepted = []
    refused = []
    for part in parts:
        result = analyze_part(rules, part, rule_name)
        if result == 'A':
            accepted.append(part)
        else:
            refused.append(part)

    # print(accepted)
    # print(refused)
    for part in accepted:
        sol1 += part.x + part.m + part.a + part.s
    return sol1

def inverse_condition(condition: tuple) -> tuple:
    check, comp, value, dest = condition
    if comp == '<':
        comp = '>'
    else:
        comp = '<'
    return (check, comp, value, dest)

# Part 2
@Timer(name="Part 2", text="Part 2......DONE: {milliseconds:.0f} ms")
def part2(data: any) -> int:
    sol2 = 0
    # p = 0
    rules, parts = data
    restrictions = {}
    for rule in rules:
        for condition in rule.conditions:
            _from = rule.name
            dest = condition[-1]
            if dest not in restrictions:
                restrictions[dest] = []
             
            print(f"{_from} [{condition[0]} {condition[1]} {condition[2]}] → {condition[3]}")
            restrictions[dest].append(f"{condition[0]} {condition[1]} {condition[2]}")
            if rule.destination == 'R':
                ic = inverse_condition(condition)
                restrictions['R'].append(f"{ic[0]} {ic[1]} {ic[2]}")
            if rule.destination == 'A':
                ic = inverse_condition(condition)
                restrictions['A'].append(f"{ic[0]} {ic[1]} {ic[2]}")
        print(f'Else {_from} → {rule.destination}')
        print()
    print(restrictions)
    # for x in range(1, 4001):
    #     for m in range(1, 4001):
    #         for a in range(1, 4001):
    #             for s in range(1, 4001):
    #                 part = Part()
    #                 part.x = x
    #                 part.m = m
    #                 part.a = a
    #                 part.s = s
                    # p += 1
                    # if p % 1000000 == 0:
                    #     print(f"Part {p}/256_000_000_000_000")
                    # result = analyze_part(rules, part)
                    # if result == 'A':
                        # sol2 += 1

    return sol2



s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
