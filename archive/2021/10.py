import re
from rich import print
import copy
from aoc import get_input
import statistics, math, random
import logging
import time
from PIL import Image, ImageDraw 
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

def bin_to_dec(string,bit):
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

DAY = 10
TEST = 0

level = logging.INFO
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)

# Parsing
if TEST:
    FILENAME = f"inputs/{DAY:02d}-test.txt"
else:
    FILENAME = f"inputs/{DAY:02d}.txt"

input = [l.strip() for l in open(FILENAME).readlines()]

start_time = time.perf_counter()

def find_corrupt_char(string, target="corrupted"):
    coppia = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    aperte = []
    for c in string:
        if c in "([{<":
            aperte.append(c)
        else:
            if aperte[-1] == coppia[c]: 
                aperte.pop()
            else:
                logging.debug(f"{string}: Stringa CORROTTA")
                if target == "corrupted":
                    return c
                else:
                    return None

    if aperte:
        logging.debug(f"{string}: Stringa incompleta")
        points = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4
        }
        to_complete = []
        for open in aperte:
            to_complete.append(coppia[open])
        to_complete.reverse()
        score = 0
        for c in to_complete:
            score = score * 5
            score += points[c]
        if target == "incomplete":
            return score

    else:
        logging.debug(f"{string}: Stringa OK")



# Part 1
sol1 = 0

punti = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

for line in input:
    c = find_corrupt_char(line, target="corrupted")
    if c:
        sol1 += punti[c]
print(f"Parte 1: \t[{sol1}]\n=======\n")

# Part 2
sol2 = 0
score = []
for line in input:
    n = find_corrupt_char(line, target="incomplete")
    if n:
        score.append(n)

score.sort()

sol2 = score[len(score)//2]
print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")
