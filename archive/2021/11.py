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

DAY = 11
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
grid = []
for l in input:
    grid.append([int(c) for c in l])


start_time = time.perf_counter()


vicinanza = [
    (1, 0),     # su
    (1, 1),     # su-dx
    (0, 1),     # dx
    (-1, 1),    # giu-dx
    (-1, 0),    # giu
    (-1, -1),   # giu-sx
    (0, -1),    # sx
    (1, -1)     # su-sx
    ]

def aumenta_energia_vicini(coord: tuple[int], grid: list[list[int]]):
    x, y = coord
    for i, j in vicinanza:
        nx = x + i
        ny = y + j
        if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
            grid[nx][ny] += 1
    return grid

def get_ready_to_flash(grid) -> list[tuple[int]]:
    ready = []
    for x in range(10):
        for y in range(10):
            if grid[x][y] > 9:
                ready.append((x,y))
    return ready

def reset_grid(grid):
    for x in range(10):
        for y in range(10):
            if grid[x][y] > 9:
                grid[x][y] = 0
    return grid

# Ritorna Bool (se ha trovato il big flash) e il numero dei flash se falso, lo step se vero

def do_steps(n_steps: int, grid: list[list[int]], output=False):
    grid = copy.deepcopy(grid)
    steps = 0
    total_flashes = 0
    boom = False
    
    if output:
        print(f"Step {steps}")
        print(grid)


    while steps < n_steps and not boom:

        flashers_this_step = set()

        # Aumento di 1 tutti i polpi
        for x in range(10):
            for y in range(10):
                grid[x][y] += 1 
        
        # Se c'è ancora qualcuno da scoppiare
        while not all(coord in flashers_this_step for coord in get_ready_to_flash(grid)):
            # Scopro quanti sono quelli che stanno per esplodere
            for coord in get_ready_to_flash(grid):
                # Se non li abbiamo già scoppiati
                if coord not in flashers_this_step:
                    # Aggiungiamo alla lista di scoppiati
                    flashers_this_step.add(coord)
                    # BOOM!
                    grid = aumenta_energia_vicini(coord, grid)
        
        # Se tutti quelli che vediamo sono già scoppiati
        grid = reset_grid(grid)
        total_flashes += len(flashers_this_step)

        steps += 1
        if output:
            print(f"Step {steps}")
            print(grid)

        if len(flashers_this_step) == 100:
            if output:
                print(f"BIG FLASH!")
                print(f"Step {steps}")
                print(grid)
            boom = True
            
    if boom:
        return boom, steps
    return boom, total_flashes

# Part 1
sol1 = 0

is_boom, sol1 = do_steps(100, grid, False)

print(f"Parte 1: \t[{sol1}]\n=======\n")

# Part 2
boom_found = False
n = 100

while not boom_found:
    boom_found, sol2 = do_steps(n, grid, False)
    n += 100

print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")
