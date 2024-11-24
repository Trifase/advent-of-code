import re
# from rich import print
import copy
from typing import NewType, final
from aoc import get_input
import statistics, math, random
import logging
import time
from PIL import Image, ImageDraw 
from collections import Counter, defaultdict

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

def lista(lista):
    for i in lista:
        print(i)

def list_to_string(lista):
    string = ''.join(str(x) for x in lista)
    return string

def string_to_list(string):
    lista = [ c for c in string ]
    return lista

def dec_to_bin(dec,bit):
    b = str(bin(int(dec))[2:]).zfill(bit)
    return b

def bin_to_dec(string, bit=2):
        dec = int(string, bit)
        return dec

def removeduplicates(lista):
  return list(dict.fromkeys(lista))

def list_replace(lst, old="1", new="10"):
    """replace list elements (inplace)"""
    i = -1
    try:
        while 1:
            i = lst.index(old, i + 1)
            lst[i] = new
    except ValueError:
        pass

def get_key_from_value(my_dict, to_find):
    for k,v in my_dict.items():
        if sorted(v) == sorted(to_find): return k
    return None

DAY = 17
TEST = 0

if TEST:
    FILENAME = f"inputs/{DAY:02d}-test.txt"
else:
    FILENAME = f"inputs/{DAY:02d}.txt"

level = logging.INFO
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)
start_time = time.perf_counter()

# Parsing
input = [l.strip() for l in open(FILENAME).readlines()]
# target area: x=20..30, y=-10..-5
input = input[0][13:].split(', ')
target_min_x, target_max_x = input[0][2:].split("..")
target_min_x, target_max_x = int(target_min_x), int(target_max_x)
target_min_y, target_max_y = input[1][2:].split("..")
target_min_y, target_max_y = int(target_min_y), int(target_max_y)

print(f"Target: {target_min_x}..{target_max_x}, {target_max_y}..{target_min_y}")
target = []
for x in range(int(target_min_x), int(target_max_x)+1):
    for y in range(int(target_min_y), int(target_max_y)+1):
        target.append([x, y])

# Part 1
sol1 = 0
max_altitudes = []
successful_launches = []

def launch(x, y):
    if x == 0:  # MISS
        return None
    probe_path = []
    probe = [0, 0]
    while probe[0] <= target_max_x and probe[1] >= target_min_y:
        if probe not in target:
            probe[0] += x
            probe[1] += y
            if x > 0:
                x -= 1
            elif x < 0:
                x += 1
            y -= 1
            probe_path.append(probe.copy())
        else:  # TARGET HIT
            max_altitudes.append(max([coord[1] for coord in probe_path]))
            successful_launches.append(1)
            return probe_path
    # TARGET MISSED
    return None


tentativi = []

# Target:  137    171 ,  -73    -98
#         min_x  max_x  max_y  min_y


try_x = target_max_x + 1
try_y = target_min_y
print(f"Ipotizzo tutti i lanci con x [0..{target_max_x + 1}] e y [{target_min_y}..{abs(target_min_y)}]")

for x in range(target_max_x + 1):
    for y in range(target_min_y, abs(target_min_y)):
        tentativi.append([x, y])

print(f"Tentativi da analizzare: {len(tentativi)}")

for t in tentativi:
    shoot(t[0], t[1])

print(f"Altitudine massima raggiunta: {max(max_altitudes)}")
sol1 = max(max_altitudes)
# Part 2
sol2 = 0
print(f"Tentativi che centrano il target: {sum(successful_launches)}")
sol2 = sum(successful_launches)

print()

if TEST:
    print("\n\n====================\nTesting environment:\n====================")
print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")
