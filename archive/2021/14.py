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

DAY = 14
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
initial_string = input[0]

def inject(polimer):
    newpolimer = defaultdict(int)
    for k,v in polimer.items():
        for j in rules[k]:
            newpolimer[j] += v
    return newpolimer

def conta(polimer):
    counter = defaultdict(int)
    for k,v in polimer.items():
        counter[k[0]] += v

    # Eccezione per l'ultima lettera, che non viene mai rimpiazzata:
    counter[initial_string[-1]] += 1

    c = Counter(counter)
    most = c.most_common()[0][1]
    least = c.most_common()[-1][1]
    return most - least

# Creo un dizionario per le regole di rimpiazzamento
rules = {}
for line in input[2:]:
    if line:
        a, b = line.split(' -> ')
        rules[a] = [a[0] + b, b + a[1]]

#Riduco la stringa iniziale a dizionario di sillabe, una volta soltanto
polimer = defaultdict(int)
for i in range(len(initial_string)-1):
    molecola = initial_string[i:i+2]
    polimer[molecola] += 1

# Mi creo una copia del dizionario originale, per la parte 2
polimer_originale = copy.deepcopy(polimer)

#Faccio 10 step
for i in range(10):
    polimer = inject(polimer)
    i += 1

sol1 = conta(polimer)

# PARTE 2

# Riprendo la copia del dizionario messa da parte
polimer = copy.deepcopy(polimer_originale)

#Faccio 30 step
for i in range(40):
    polimer = inject(polimer)
    i += 1


sol2 = conta(polimer)

print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")



