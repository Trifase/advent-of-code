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

DAY = 5
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

# Part 1
sol1 = 0

def has_double(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False


def is_banned(string):
    for sub in ["ab", "cd", "pq", "xy"]:
        if sub in string:
            return True
    return False

def wovel_count(string):
    return sum(1 for c in string if c in "aeiou")

def is_naughty(string):
    if is_banned(string):
        return True
    elif not has_double(string):
        return True
    elif wovel_count(string) < 3:
        return True
    else:
        return False

c = 0
for stringa in input:
    if not is_naughty(stringa):
        c += 1
    # print("Naughty" if is_naughty(stringa) else "Nice", stringa)
sol1 = c


# Part 2
def has_xyx(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def has_double_double(string):
    for i in range(len(string)-1):
        substring = string[i:i+2]
        if string[i+2:].count(substring) > 0 or string[:i].count(substring) > 0:
            return True
    return False

sol2 = 0
for string in input:
    if has_double_double(string) and has_xyx(string):
        sol2 += 1


if TEST:
    print("\n\n====================\nTesting environment:\n====================")
print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")
