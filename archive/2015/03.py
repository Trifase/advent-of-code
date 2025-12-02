import re
# from rich import print
import copy
from typing import NewType, final
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

DAY = 3
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
# input = ["^v", "^>v<", "^v^v^v^v^v"]

# Part 1
sol1 = 0

s_coord = (0, 0)

dir = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

for line in input:
    case = set()

    case.add(s_coord)
    for c in line:
        s_coord = tuple(sum(x) for x in zip(s_coord, dir[c]))
        case.add(s_coord)
sol1 = len(case)


# Part 2

for line in input:
    s_coord = (0, 0)
    r_coord = (0, 0)
    robot = False

    case = set()
    case.add(s_coord)

    for c in line:
        if robot:
            r_coord = tuple(sum(x) for x in zip(r_coord, dir[c]))
            case.add(r_coord)
            robot = False
        else:
            s_coord = tuple(sum(x) for x in zip(s_coord, dir[c]))
            case.add(s_coord)

            robot = True

sol2 = len(case)

if TEST:
    print("\n\n====================\nTesting environment:\n====================")
print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")
