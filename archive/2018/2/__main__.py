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

def removeduplicates(lista):
  return list(dict.fromkeys(lista))

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

day = 2
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

def check2(string):
    for c in string:
        if string.count(c) == 2:
            return True
    return False

def check3(string):
    for c in string:
        if string.count(c) == 3:
            return True
    return False
  
count2 = 0
count3 = 0
for line in lines:
    # print(line, end=": ")
    if check2(line):
        count2 += 1
        # print("2✓",end=" ")
    # else:
        # print("  ",end=" ") 
    if check3(line):
        count3 += 1
        # print("3✓",end=" ")
    # print()

# part1
soluzione1 = count2*count3
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 

boxlist = []
for line in lines:
    templist = [c for c in line]
    boxlist.append(templist)
# print(boxlist)

# boxlist = []
# for line in lines:
#     tempset = {c for c in line}
#     boxlist.append(tempset)
# # print(boxlist)

nset = 0
# print(len(boxlist[1].difference(boxlist[4])))
trovato = set()

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



for lst1 in boxlist:
    for lst2 in boxlist:
        # if lst1 == lst2:
        #     break
        if len(difference(lst1, lst2)) == 1:
            # print(f'Trovate due liste quasi identiche: sono:')
            # print(lst1)
            # print(lst2)
            # print(f'{boxlist.index(lst1)} - {boxlist.index(lst2)}: {difference(lst1, lst2)}') 
        # if len(difference(lst1, lst2)) == 1:
            trovato = intersection(lst1, lst2)
        #     print(trovato)
            # print(set)
            # print(boxlist[nset])
            # break

soluzione2 = list_to_string(trovato)
# for c in trovato:
#     soluzione2 += c
      
# print(trovato)            


# soluzione2 = "NON LO SO"
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




