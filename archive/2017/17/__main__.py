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
from time import perf_counter 

init(autoreset=True)

t1_start = perf_counter() 

pp = pprint.PrettyPrinter(indent=3)

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

    #(.+) \((\d+)\)(?: \-\> (.+))?
    #for line in lines
    #x, y = rematch(r"REGEXP", line).groups()

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

day = 17
test = 0

# Parsing
if test == 1:
    FILENAME = f"{day}-test.txt"
else:
    FILENAME = f"{day}.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono
    # moves = lines[0].split(",") #una nuova lista degli elementi splittati
    # lines = [int(n) for n in lines] #converte tutta la lista in int
    # starts = [int(i[-3:]) for i in lines] #[512, 191]
print(lines)
registers = {}

i = 0
sound = 0
while i <= len(lines):
    command = lines[i]
    register = command[4]
    if register not in registers:
        registers[register] = 0
    # print(f'[{i}] DEBUG: -command: {command} -register: {register} -value: {command[6:]} ')
    
    if command.startswith('snd'):
        sound = registers[register]
        print(f'[{i}]: Riproduco suono nel registro [{register}]: {sound}')
        i += 1

    if command.startswith('set'):
        try:
            value = int(command[6:])
        except ValueError:
            value = registers[command[6:]]
        registers[register] = value
        print(f'[{i}]: Setto registro [{register}]: {value}')
        i += 1

    if command.startswith('add'):
        try:
            value = int(command[6:])
        except ValueError:
            value = registers[command[6:]]
        registers[register] = registers[register] + value
        print(f'[{i}]: Aggiungo al registro [{register}] {value}: {registers[register]}')
        i += 1

    if command.startswith('mul'):
        try:
            value = int(command[6:])
        except ValueError:
            value = registers[command[6:]]
        registers[register] = registers[register] * value
        print(f'[{i}]: Moltiplico il registro [{register}] di {value}: {registers[register]}')
        i += 1

    if command.startswith('mod'):
        try:
            value = int(command[6:])
        except ValueError:
            value = registers[command[6:]]
        registers[register] = registers[register]%value
        print(f'[{i}]: Modulo il registro [{register}] per {value}: {registers[register]}')
        i += 1

    if command.startswith('rcv'):
        if registers[register] != 0:
            print(f'[{i}]: Ultimo suono riprodotto: {sound}')
            i += len(lines)+1
        else:
            print(f'[{i}]: {registers[register]} è 0. Vado avanti.')
            i += 1

    if command.startswith('jgz'):
        try:
            value = int(command[6:])
        except ValueError:
            value = registers[command[6:]]
        if registers[register] > 0:
            print(f'[{i}]: Salto di {value}: -> {i + value}')
            i += value
        else:
            print(f'[{i}]: {registers[register]} è minore o uguale a zero. Vado avanti.')
            i += 1




soluzione1 = sound
print(f'\n{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 


# print("----")
# soluzione2 = "UNKNOWN"
# print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 

t1_stop = perf_counter() 
print(f'Tempo esecuzione: {t1_stop-t1_start}') 