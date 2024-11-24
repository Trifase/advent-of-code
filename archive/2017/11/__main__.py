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

day = 11
test = 0

# Parsing
if test == 1:
    FILENAME = f"{day}-test.txt"
else:
    FILENAME = f"{day}.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono
    moves = lines[0].split(",") #una nuova lista degli elementi splittati
    # lines = [int(n) for n in lines] #converte tutta la lista in int
    # lines = [int(i) for i in input]
# print(lines)
# # print(moves)
#x,y,z
# origine = (0,0) #vert, orizz
origine = (0,0,0)
nw,n,ne,sw,s,se = 0,0,0,0,0,0
x,y,z = 0,0,0
nord,destra = 0,0
print(moves)
manhattans = []
# moves = ('se','sw','se','sw','sw')
def cube_distance(origine, destinazione):
    return (abs(origine[0] - destinazione[0]) + abs(origine[1] - destinazione[1]) + abs(origine[2] - destinazione[2]))//2


for move in moves:
    if move == 'nw':
        nw += 1
        y +=1
        x -= 1
        nord += 1
        destra -= 1
    if move == 'n':
        n += 1
        y += 1
        z -= 1
        nord += 1
    if move == 'ne':
        ne += 1
        nord += 1
        destra += 1
        z -= 1
        x += 1
    if move == 'sw':
        sw += 1
        nord -= 1
        destra -= 1
        z += 1
        x -=1
    if move == 's':
        s += 1
        nord -= 1
        z += 1
        y -= 1
    if move == 'se':
        se += 1
        nord -= 1
        destra += 1
        y -= 1
        x += 1
    destinazione = (x,y,z)
    man = cube_distance(origine,destinazione)
    manhattans.append(man)
    print(f'{move}: {x},{y},{z} : manhattan = {man}')

def axial_to_cube(hex):
    x = hex[0]
    z = hex[1]
    y = -x-z
    return (x, y, z)
# x1 = se-nw
# y1 = ne-sw
# z1 = n-s
# destinazione = (x1,y1,z1)
destinazione = (nord,destra)
destinazione = (x,y,z)

print(f'lunghezza comandi: {len(moves)}')
print(f'comandi eseguiti: {nw,n,ne,sw,s,se}: {nw+n+ne+sw+s+se}')
print("---")
print(f'destinazione = {destinazione}')
# print(f'in cube = {axial_to_cube(destinazione)}')
print("-")
print(f'origine = {origine}')
# print(f'in cube = {axial_to_cube(origine)}')


# print(f'destinazionoe2 = {destinazione2}')


print("-")
print(f'Manhattan = {cube_distance(origine,destinazione)}')
print(f'Manhattan massima: {max(manhattans)}')

# print(distance(origine,destinazione))

print()
soluzione1 = "UNKNOWN"
# soluzione1 = find_first_node(tree)
# 
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 
print("----")
soluzione2 = soluzione1
# soluzione2 = steps-last_ID-1
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




