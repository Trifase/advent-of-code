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

pp = pprint.PrettyPrinter(indent=3)

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

def lista(lista):
    for i in lista:
        print(i)

def list_to_string(lista):
    string = ''.join(x for x in lista)
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

test = 0

# Parsing
if test == 1:
    FILENAME = "1-test.txt"
else:
    FILENAME = "1.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono


# part1
sol1 = 0

for i in lines:
    mass = math.floor(int(i)/3)-2
    sol1 += mass

print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{sol1}]') 

# part 2
sol2 = 0
# test = ['1969', '100756']
module_fuel = 0
for i in lines:
    mass = int(i)
    fuel = 0
    while mass > 0:
       fuel = math.floor(int(mass)/3)-2
       if fuel < 0:
           break
       module_fuel += fuel
    #    print(f'{mass} - {fuel} - {module_fuel}')
       mass = fuel
    sol2 += module_fuel
    module_fuel = 0
    # print(sol2)

    

print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{sol2}]') 



