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

DAY = 21
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
p1_pos = 0
p1_pos = int(input[0].split("position: ")[1])
p1_score = 0
p2_pos = int(input[1].split("position: ")[1])
p2_score = 0


def deterministic_dice():
    n = 1
    while True:
        yield n
        n += 1
        if n == 101:
            n = 1



dice = deterministic_dice()
print(p1_pos)
print(p2_pos)
def parte1(p1, p2):
    rolls = 0
    dice = deterministic_dice()
    score1, score2 = 0, 0
    while True:
        s1 = next(dice) + next(dice) + next(dice)
        rolls += 3
        p1 = ((p1 + s1 - 1) % 10) + 1
        score1 += p1
        if score1 >= 1000:
            print(f"Ha vinto il Player 1 dopo {rolls} lanci con un punteggio di {score1}. Il punteggio di Player 2 è {score2}")
            return rolls * score2

        s2 = next(dice) + next(dice) + next(dice)
        rolls += 3
        p2 = ((p2 + s2 - 1) % 10) + 1
        score2+= p2
        if score2 >= 1000:
            print(f"Ha vinto il Player 2 dopo {rolls} lanci con un punteggio di {score2}. Il punteggio di Player 1 è {score1}")
            return rolls * score1

sol1 = parte1(p1_pos, p2_pos)
# Part 1
# sol1 = 0



# Part 2
sol2 = 0



if TEST:
    print("\n\n====================\nTesting environment:\n====================")
print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")
