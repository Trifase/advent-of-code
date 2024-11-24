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

day = 1
test = 0

# Parsing
if test == 1:
    FILENAME = f"{day}-test.txt"
else:
    FILENAME = f"{day}.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono
    # input = lines[0].split(",") #una nuova lista degli elementi splittati
    lines = [int(n) for n in lines] #converte tutta la lista in int

twice = False
frequency = 0
frequencies = {0}
i = 0
while twice == False:
    # print(f'DEBUG: frequenza corrente {frequency}, istruzione #{i%len(lines)}: {lines[i%len(lines)]}',end=" ")
    frequency += lines[i%len(lines)]
    # print(f'nuova frequenza: {frequency}.',end=" ")
    if frequency in frequencies:
        twice = True
        print(f'Trovata frequenza doppia: {frequency}')
        break
    # print(f'Frequenza NUOVA, prossima istruzione #{i+1}')
    frequencies.add(frequency)
    i += 1

# part1
soluzione = "NON ANCORA TROVATA"
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{frequency}]') 



