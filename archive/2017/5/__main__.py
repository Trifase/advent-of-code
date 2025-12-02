import itertools
import math
import os
import re
import sys
from collections import defaultdict,Counter
from functools import partial
from typing import Dict, List, Tuple
import pprint
from colorama import init, Fore, Back,Style

init(autoreset=True)

pp = pprint.PrettyPrinter(indent=3)

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

def verticallist(lista):
    for i in lista:
        print(i)

def list_to_string(lista):
    string = ''.join(x for x in lista)
    return string

def string_to_list(string):
    lista = [c for c in string ]
    return lista

def dec_to_bin(dec,bit):
    b = str(bin(int(dec))[2:]).zfill(bit)
    return b

def bin_to_dec(string,bit):
        dec = int(string, bit)
        return dec

def intersection(lista1, lista2):  
    lst3 = []
    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            lst3.append(lista1[i]) 
    return lst3 

def difference(lista1, lista2): 
    lst3 = []
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            lst3.append(lista1[i]) 
    return lst3 

day = 5
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
    # lines = [int(n) for n in lines] #converte tutta la lista in int
lines = [int(i) for i in lines]
print()
print(lines)


# lines = [0,3,0,1,-3]

lines_bk = lines.copy()
# 
# parte1
i = 0
step = 0
exit = False
while exit == False:
    try:
        goto = lines[i]
        lines[i] += 1
        i += goto
        step += 1
    except IndexError:
        exit = True
        print("Uscito!")

lines = lines_bk.copy()
# parte2
i = 0
step2 = 0
exit = False
while exit == False:
    try:
        goto = lines[i]
        if goto >= 3:
            lines[i] -= 1
        else:    
            lines[i] += 1
        i += goto
        step2 += 1
    except IndexError:
        exit = True
        print("Uscito!")
        print(lines)



soluzione1 = "UNKNOWN"
soluzione1 = step
# 
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 
print("----")

soluzione2 = step2

print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




