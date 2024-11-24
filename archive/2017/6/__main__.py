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

day = 6
test = 0

# Parsing
if test == 1:
    FILENAME = f"{day}-test.txt"
else:
    FILENAME = f"{day}.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono
    input = lines[0].split("\t") #una nuova lista degli elementi splittati
    # lines = [int(n) for n in lines] #converte tutta la lista in int
    lines = [int(i) for i in input]
# print(lines)
print()

stacks = lines.copy()
print(stacks)
# [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
# stacks = [0, 2, 7, 0]
print()
def redprint(stacks,id):
    for i in range(len(stacks)):
        if i == id:
            print(f'{Fore.GREEN}[{Fore.RED}{stacks[i]}{Fore.GREEN}]',end=", ")
        elif i == len(stacks)-1:
            print(stacks[i],end="")
        else:
            print(stacks[i],end=", ")
    return

def step(stacks):
    high_value = max(stacks)
    high_id = stacks.index(high_value)
    # print(f'Cerco stacks: [',end="")
    # redprint(stacks,high_id)
    # print("]")
    # print(f'Trovato valore più alto. stacks[{high_id}] = {high_value}. Aggiungo 1 ai prossimi {high_value} indici.')
    stacks[high_id] = 0
    i = high_id
    while high_value != 0:
        i += 1
        stacks[i%len(stacks)] += 1
        high_value -= 1
    # print(f'Nuovo stacks: {stacks}')
    # print("--")
    return 

steps = 0
states = []
found = False
last_ID = 0
last_step = 0

while found == False:
    steps += 1
    step(stacks)
    # print(f'steps: {steps}')
    if stacks in states:
        last_ID = states.index(stacks)
        found = True
        print(f'Ultimo ID: {len(states)-1}')
        break

    states.append(stacks.copy())    


print()
print(f'Loop infinito. Ci sono volute {steps} iterazioni.')
lastloop = stacks.copy()
print(f'Ultimo stato del loop: {lastloop}. È all\' index {last_ID}')







soluzione1 = "UNKNOWN"
soluzione1 = steps
# 
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 
print("----")

soluzione2 = steps-last_ID-1
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




