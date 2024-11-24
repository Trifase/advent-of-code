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

day = 16
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
    # starts = [int(i[-3:]) for i in lines] #[512, 191]
# print(lines)

dancefloor = "abcdefghijklmnop"
step1 = "abcdefghijklmnop"
step2 = "eojfmbpkldghncia"
dict = str.maketrans(step1,step2)
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#a b c d e f g h i j k  l  m  n  o  p
#e o j f m b p k l d g  h  n  c  i  a


# def rearrange():
#     reference = dancefloor.copy()
#     dancefloor[0] = reference[4]
#     dancefloor[1] = reference[14]
#     dancefloor[2] = reference[9]
#     dancefloor[3] = reference[5]
#     dancefloor[4] = reference[12]
#     dancefloor[5] = reference[1]
#     dancefloor[6] = reference[15]
#     dancefloor[7] = reference[10]
#     dancefloor[8] = reference[11]
#     dancefloor[9] = reference[3]
#     dancefloor[10] = reference[6]
#     dancefloor[11] = reference[7]
#     dancefloor[12] = reference[13]
#     dancefloor[13] = reference[2]
#     dancefloor[14] = reference[8]
#     dancefloor[15] = reference[0]
# def rearrange(string):
#     reference = string
#     dancefloor = reference.translate(dict)



#TEST
# input = ['s1,x3/4,pe/b']
# dancefloor = 'abcde'
# moves = input[0].split(",")
# # moves = ['s1','x3/4','pe/b']
# print(moves)


# #TEST
# #parte1
def dance(string):
    dancefloor = list(string)
    for move in moves:
            if move.startswith('s'):
                n = int(move[1:])
                for i in range(n):
                    dancefloor.insert(0, dancefloor.pop()) 
            
            if move.startswith('x'):
                instr = move[1:].split("/")
                reference = dancefloor.copy()
                dancefloor[int(instr[0])] = reference[int(instr[1])]
                dancefloor[int(instr[1])] = reference[int(instr[0])]
            
            if move.startswith('p'):
                instr = move[1:].split("/")
                reference = dancefloor.copy()
                dancefloor[reference.index(instr[0])] = reference[reference.index(instr[1])]
                dancefloor[reference.index(instr[1])] = reference[reference.index(instr[0])]
                
    dancefloor = "".join(dancefloor)
    return dancefloor


step1 = "abcdefghijklmnop"
print("[0]: abcdefghijklmnop")
print("-")
for i in range(999999984,1000000000):
    step2 = dance(step1)
    step1 = step2
    print(f'[{i+1}]: {step2}')
    # if step2 == "abcdefghijklmnop":
    #     print("ALT!")
    #     print(f'[{i+1}]: {step2}')
    #     quit()
# dancefloor = "".join(dancefloor)
# print()
# soluzione1 = "UNKNOWN"
soluzione1 = step2
# 
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 

#parte2
# step1 = "abcdefghijklmnop"
# step2 = "eojfmbpkldghncia"
# dict = str.maketrans(step1,step2)

# dancefloor = "abcdefghijklmnop"
# print(f'Inizio da: {dancefloor}')
# for i in range(32):
#     dancefloor = dancefloor.translate(dict)
#     print(f'[{i}]: {dancefloor}')
#     # if dancefloor == step1:
#     #     print("ALT!")
#     #     quit()

#     if i%10000000 == 0:
#         t1_stop = perf_counter() 
#         print(f'Iterati: {i}\tTempo esecuzione: {t1_stop-t1_start}') 
#         t1_start = perf_counter() 
# print(dancefloor)

# rearrange(dancefloor)

# for i in range(1000000000):
#     rearrange()
#     if i%10000000 == 0:
#         print(i)
# dancefloor = "".join(dancefloor)
# # # print(dancefloor)
# dancefloor = "abcdefghijklmnop"

# print("----")
# soluzione2 = "UNKNOWN"
# soluzione2 = dancefloor
# print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 
# print(len(moves))

t1_stop = perf_counter() 
print(f'Tempo esecuzione: {t1_stop-t1_start}') 