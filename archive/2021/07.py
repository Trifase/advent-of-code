import re
from rich import print
import copy
from aoc import get_input
import statistics, math


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

DAY = 7
TEST = 0


# Parsing
if TEST:
    FILENAME = f"inputs/{DAY:02d}-test.txt"
else:
    FILENAME = f"inputs/{DAY:02d}.txt"


lines = [l.strip() for l in open(FILENAME).readlines()]

crabs = [int(x) for x in lines[0].split(",")]


def fuel_to_align_crabs_median(crabs: list[int]) -> int:
    fuel = 0
    median = int(statistics.median(crabs))
    print(f"La mediana esatta è {statistics.median(crabs)}")
    for crab in crabs:
        fuel += abs(crab - median)
    print(f"Usando {median} come target, il totale dei consumi è {fuel}") 
    return fuel

def fuel_to_align_crabs_mean(crabs: list[int]) -> int:
    def calculate_crab_consumption_triangular(crabs: list[int], mean: int) -> int:
        total_fuel = 0
        for crab in crabs:
            fuel = 0
            distance  = abs(crab - mean)
            fuel = int(distance * (distance + 1) / 2)
            total_fuel += fuel
        return total_fuel
    print(f"La media esatta è: {statistics.mean(crabs)}")
    mean_up = math.ceil(statistics.mean(crabs))
    mean_down = math.floor(statistics.mean(crabs))
    possible_solutions = []
    for mean in [mean_down, mean_up]:  # boh chissà come fare a capire quale è quella giusta
        print(f"Usando {mean} come target, il totale dei consumi è {calculate_crab_consumption_triangular(crabs, mean)}")
        possible_solutions.append(calculate_crab_consumption_triangular(crabs, mean))
    return min(possible_solutions)

# Part 1
sol1 = fuel_to_align_crabs_median(crabs)
print(f"Parte 1: \t[{sol1}]\n")

# Part 2
sol2 = fuel_to_align_crabs_mean(crabs)
print(f"Parte 2: \t[{sol2}]")

