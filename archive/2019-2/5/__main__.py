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

day = 5
test = 0

# Parsing
if test == 1:
    FILENAME = f"{day}-test.txt"
else:
    FILENAME = f"{day}.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    # lines = [line.strip() for line in file] #una lista di tutte le righe così come sono
    input = file[0].split(",") #una lista di tutte le righe così come sono
    input = [int(n) for n in input]

# part1

sol2 = 0
i = 0
values = 0

while input[i] != 99:
    if input[i][-1] == 1: 
    if input[i][-1] == 2: 
    if input[i][-1] == 3: 
    if input[i][-1] == 4: 


comman
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{sol2}]') 



