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

DAY = 15
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
matrix = []
for l in input:
    matrix.append([int(x) for x in l])

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.breadth_first import BreadthFirstFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.finder.a_star import AStarFinder

grid = Grid(matrix=matrix)
start = grid.node(0, 0)
end = grid.node(len(matrix[0]) - 1, len(matrix) - 1)

algo = "astar"
algo = "dijkstra"

if algo == "astar":
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
elif algo == "dijkstra":
    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
else: 
    finder = BreadthFirstFinder(diagonal_movement=DiagonalMovement.never)
    
path, runs = finder.find_path(start, end, grid)



print('[Part 1] operations:', runs, 'path length:', len(path))
# print(grid.grid_str(path=path, start=start, end=end))
sol1 = 0
for x, y in path:
    # print(f"{x},{y}: {matrix[y][x]}")
    sol1 += matrix[y][x]
sol1 -= matrix[0][0]



# Part 2
sol2 = 0
giant_matrix = []

size = len(matrix)
giant_matrix = [[0 for i in range(size*5)] for j in range(size*5)]
for y in range(5):
    for x in range(5):
        for j in range(size):
            for i in range(size):
                giant_matrix[y*size + j][x*size + i] = (matrix[j][i] + y + x - 1) % 9 + 1

grid = Grid(matrix=giant_matrix)
start = grid.node(0, 0)
end = grid.node(len(giant_matrix[0]) - 1, len(giant_matrix) - 1)
# finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

path, runs = finder.find_path(start, end, grid)
print('[Part 2] operations:', runs, 'path length:', len(path))

for x, y in path:
    sol2 += giant_matrix[y][x]
sol2 -= giant_matrix[0][0]


if TEST:
    print("====================\nTesting environment:\n====================")
if algo == "astar":
     print("Using: A*\n")
elif algo == "dijkstra":
    print("Using: Dijkstra\n")

print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")



