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

day = 15
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
    starts = [int(i[-3:]) for i in lines] #[512, 191]
# print(lines)


#TEST
# starts = [65,8921]
factorA = 16807
factorB = 48271
divider = 2147483647
#Ogni generatore inizia con start, moltiplica per factorX, e poi modulo con divider. converti in bin 32 con leading0 e confronta le ultime 16 cifre.
# restituisci quante coppie sono uguali

i = 0
A = starts[0]
B = starts[1]
c = 0
while i < 5000000:
    A = A*factorA%divider
    B = B*factorB%divider
    if i%(500000) == 0: 
        print(i) #vedo dove è arrivato per occupare il tempo (occupa 3.8 secondi di esecuzione)
    while A%4 != 0:
        A = A*factorA%divider
    while B%8 !=0:
        B = B*factorB%divider
    if "{0:032b}".format(A)[16:] == "{0:032b}".format(B)[16:]:
        c += 1
    i += 1
    # print(f'[{i}] A: {A} - B: {B}\n{"{0:032b}".format(A)}\n{"{0:032b}".format(B)}')
print(f'--')
print(f'sol: {c}')


print()
soluzione1 = "UNKNOWN"
soluzione1 = c
# 
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 
print("----")
soluzione2 = soluzione1
# soluzione2 = steps-last_ID-1
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 

t1_stop = perf_counter() 
print(f'Tempo esecuzione: {t1_stop-t1_start}') 