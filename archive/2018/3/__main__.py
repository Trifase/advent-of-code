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

def verticallist(lista):
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

day = 3
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
# print(lines)
rettangoli = []
for line in lines:
    square = line.split()
    square.remove('@')
    square_index = int(square[0][1:])
    square_coord = square[1].split(",")
    square_coordx = int(square_coord[0])
    square_coordy = int(square_coord[1].strip(':'))
    square_size  = square[2].split("x")
    square_sizex = int(square_size[0])
    square_sizey = int(square_size[1])
    # print(f'Quadrato numero #{square_index}: inizia a ({square_coordx},{square_coordy}) ed è grande {square_sizex}x{square_sizey}.')
    square = [square_index, square_coordx, square_coordy, square_sizex, square_sizey]
    rettangoli.append(square)

print("Letti tutti i rettangoli.")

def draw_rect(index,coordx,coordy,sizex,sizey): #1, (1,3), (4x4)
    rectangle = {(coordx,coordy)}
    for x in range(coordx,coordx+sizex): #1-1+4: 1-5
        for y in range(coordy,coordy+sizey): #3-3+4: 3-7
            rectangle.add((x,y))
    return rectangle

cloth = set()
claimed = set()
noclaimed = []
print("Calcolo intersezioni.")
n = 0
for rect in rettangoli:
    print(f'Calcolo rettangolo #{n}...',end="")
    for point in draw_rect(rect[0],rect[1],rect[2],rect[3],rect[4]):
        if point in cloth:
            claimed.add(point)
        cloth.add(point)

    n += 1
    print("Fatto.")
# print(cloth)
# print(claimed)

soluzione1 = len(claimed)
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 

print("Cerco rettangolo intatto.")
n = 0

claimedcounter = 0
for rect in rettangoli:
    for point in draw_rect(rect[0],rect[1],rect[2],rect[3],rect[4]):
        if point in claimed:
            claimedcounter += 1
    if claimedcounter == 0:
        noclaimed = rect
    claimedcounter = 0



soluzione2 = noclaimed[0]
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




