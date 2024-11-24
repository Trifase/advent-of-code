import itertools
import math
import os
import re
import sys
from collections import defaultdict
from functools import partial
from typing import Dict, List, Tuple
import pprint
from colorama import init, Fore, Back,Style

init(autoreset=True)

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

# Parsing
with open("13.txt") as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una floor di tutte le righe così come sono

# print(lines)
time = int(lines[0])
# print(time)
bus = list(lines[1].split(","))
# print(bus)
while "x" in bus:
    bus.remove("x")
# print(bus)
# print("Sorto")
bus = [int(i) for i in bus]
bus.sort()
# print(bus)
number = []
etas = []
diff = []


print(f'Time\t\tBus#\tETA\tDIFF')
for i in bus:
    resto = time%i
    eta = i*math.floor(time/i)+(i)
    number.append(i)
    etas.append(eta)
    diff.append(eta-time)
    print(f'{time}\t\t{i}\t{eta}\t{(eta-time)}')
    # print(f'{resto}', end=" ")
# print(f'NUMBERS: {number}')
# print(f'ETAS: {etas}')
# print(f'DIFF: {diff}')
faster = etas.index(min(etas))
print()
print(f'Il bus da prendere è il numero {number[faster]}, che arriva alle {etas[faster]}, cioè fra {diff[faster]} minuti. Sbrigati!!')
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{number[faster]*diff[faster]}]')