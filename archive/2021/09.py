import re
from rich import print
import copy
from aoc import get_input
import statistics, math
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

DAY = 9
TEST = 0

level = logging.INFO
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)

# Parsing
if TEST:
    FILENAME = f"inputs/{DAY:02d}-test.txt"
else:
    FILENAME = f"inputs/{DAY:02d}.txt"

heightmap = [l.strip() for l in open(FILENAME).readlines()]

start_time = time.perf_counter()



def is_low_point(heightmap: list[list[int]], coords: tuple) -> bool:
    def find_neighbours_values(heightmap: list[list[int]], coords: tuple):
        row, col = coords
        maxrow = len(heightmap) - 1
        maxcol = len(heightmap[0]) - 1
        logging.debug(f"Cerco i vicini di {row}, {col}")
        su = heightmap[row - 1][col] if row != 0 else 9
        logging.debug(f"Su è {su}")
        giu = heightmap[row + 1][col] if row != maxrow else 9
        logging.debug(f"Giù è {giu}")
        dx = heightmap[row][col + 1] if col != maxcol else 9
        logging.debug(f"Dx è {dx}")
        sx = heightmap[row][col - 1] if col != 0 else 9
        logging.debug(f"Sx è {sx}")
        return [int(su), int(dx), int(giu), int(sx)]
    x, y = coords
    this_point = int(heightmap[x][y])
    neighboors = find_neighbours_values(heightmap, coords)
    if all(this_point < n for n in neighboors):
        return True
    return False

def flood_basin(heightmap: list[list[int]], start: tuple, basin) -> list[tuple[int]]:
    row, col = start
    basin.append((row, col))  # Aggiungo la cella alla lista
    maxrow = len(heightmap) - 1  # limiti
    maxcol = len(heightmap[0]) - 1  
    
    su = (row - 1, col) if (row != 0) and (heightmap[row - 1][col] != '9') else None  # non è un limite e non è un 9
    giu = (row + 1, col) if (row != maxrow) and (heightmap[row + 1][col] != '9') else None
    dx = (row, col + 1) if (col != maxcol) and (heightmap[row][col + 1] != '9') else None
    sx = (row, col - 1) if (col != 0) and (heightmap[row][col - 1] != '9') else None
    logging.debug(f"Basin [{len(basin)}]: {basin}")
    logging.debug(f"{row, col} Ho trovato le seguenti celle su cui posso floddare: {[su, dx, giu, sx]}")

    for cell in [su, dx, giu, sx]:
        if cell:
            if cell not in basin:
                logging.debug(f"Mi sposto su {cell}")
                flood_basin(heightmap, cell, basin)
    return basin

# Part 1
sol1 = 0

low_points = {}
for x in range(len(heightmap)):
    for y in range(len(heightmap[0])):
        if is_low_point(heightmap, (x,y)):
            low_points[(x, y)] = int(heightmap[x][y])

sol1 = sum(low_points.values()) + len(low_points) 
print(f"Parte 1: \t[{sol1}]\n=======\n")


# Part 2
sol2 = 0

basins = {}
import random
for start in low_points.keys():
    rep_value = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    basin = []
    basin = flood_basin(heightmap, start, basin)
    basins[start] = len(basin)



top3 = sorted([n for n in basins.values()], reverse=True)[:3]
sol2 = math.prod(top3)

print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")
