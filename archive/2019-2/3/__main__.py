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
    wire1 = lines[0].split(",")
    wire2 = lines[1].split(",")
    # input = [int(n) for n in input]

#Begin
pointswire1 = {(0,0)}
pointswire2 = {(0,0)}
x1 = 0
y1 = 0
x2 = 0
y2 = 0
for command in wire1:
    D = command[0]
    n = int(command[1:])
    if D == "R":
        for i in range(n):
            pointswire1.add((x1+i,y1))
        x1 += n
    if D == "D":
        for i in range(n):
            pointswire1.add((x1,y1-i))
        y1 -= n
    if D == "L":
        for i in range(n):
            pointswire1.add((x1-i,y1))
        x1 -= n
    if D == "U":
        for i in range(n):
            pointswire1.add((x1,y1+i))
        y1 += n

for command in wire2:
    D = command[0]
    n = int(command[1:])
    if D == "R":
        for i in range(n):
            pointswire2.add((x2+i,y2))
        x2 += n
    if D == "D":
        for i in range(n):
            pointswire2.add((x2,y2-i))
        y2 -= n
    if D == "L":
        for i in range(n):
            pointswire2.add((x2-i,y2))
        x2 -= n
    if D == "U":
        for i in range(n):
            pointswire2.add((x2,y2+i))
        y2 += n


# part1
intersections = pointswire1.intersection(pointswire2)
print("Punti in comune",end=": ")
print(intersections)

listaintersezioni=[]
for tupla in intersections:
    mandist = abs(tupla[0])+abs(tupla[1])
    listaintersezioni.append((mandist, tupla))
listaintersezioni.sort()
listaintersezioni.pop(0)
print(f"Punto più vicino: {listaintersezioni[0][1]} - Manhattan Distance:{listaintersezioni[0][0]}")

print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{listaintersezioni[0][0]}]') 


# part 2
def StepsTo(tuple,wire):
    counter = 0
    x = 0
    y = 0
    posx = tuple[0]
    posy = tuple[1]
    index = 0
    trovato = False
    while trovato == False:
        command = wire[index]
        D = command[0]
        n = int(command[1:])
        if D == "R":
            for i in range(n):
                counter += 1
                x += 1
                if x == posx and y == posy:
                    trovato = True
                    break
        if D == "D":
            for i in range(n):
                counter += 1
                y -= 1
                if x == posx and y == posy:
                    trovato = True
                    break
        if D == "L":
            for i in range(n):
                counter += 1
                pointswire1.add((x1-i,y1))
                x -= 1
                if x == posx and y == posy:
                    trovato = True
                    break
        if D == "U":
            for i in range(n):
                counter += 1
                y += 1
                if x == posx and y == posy:
                    trovato = True
                    break
        index += 1
        if x == posx and y == posy:
            trovato = True
            break
    return counter

intersections.remove((0,0))
contapassi = []

for X in intersections:
    contapassi.append(StepsTo(X,wire1)+StepsTo(X,wire2))
    print(f'Passi per {X}: {StepsTo(X,wire1)}+{StepsTo(X,wire2)} = {StepsTo(X,wire1)+StepsTo(X,wire2)}')

print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{min(contapassi)}]')