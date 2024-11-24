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

day = 2
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
sol1 = 0
linesbk = input.copy()

def run(noun,verb,lines):
    # noun = 12
    # verb = 2
    i = 0
    instr = 0
    lines[1] = noun
    lines[2] = verb
    # print(f'inizio modificato: {lines}')
    print(f'noun = {noun}, verb = {verb}', end=": ")
    while True:
        if lines[i] == 1:
            # print(f"caso 1: i prossimi valori sono {lines[i+1]}, {lines[i+2]}, {lines[i+3]}")
            # print(f'{lines[lines[i+1]]}+{lines[lines[i+2]]} = {lines[lines[i+1]]+lines[lines[i+2]]} da mettere in {lines[i+3]}')
            lines[lines[i+3]] = lines[lines[i+1]]+lines[lines[i+2]]
            i += 4
            # print(lines)
        elif lines[i] == 2:
            # print("2")
            lines[lines[i+3]] = lines[lines[i+1]]*lines[lines[i+2]]
            i += 4
            # print(lines)
        elif lines[i] == 99:
            print(lines[0])
            # print("ALT! NOVANTANOVE")
            # print(lines)
            return lines[0]
        else: 
            print("FAIL")
            break

numbers = input.copy()
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{run(12,2,numbers)}]') 
numbers = input.copy()

# part 2
sol2 = 0
goodnoun=0
goodverb=0

for noun in range(100):
    for verb in range(100):
        numbers = input.copy()
        if run(noun,verb,numbers) == 19690720: #19690720
            # print(f'Trovati: {noun} e {verb} danno 19690720')
            sol2 = 100*noun+verb
            goodnoun = noun
            goodverb = verb
            break # questo break ferma solo il range di verb, ma non di noun
            
print(f'noun = {goodnoun}, verb = {goodverb}')
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{sol2}]') 



