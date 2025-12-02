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
# print(lines)
mystring = lines[0]

print()
# print(input)

def HasUnits(stringa):
    hasunits = False
    stringa = string_to_list(stringa)
    i = 0
    finished = False
    while finished == False:
        if i == len(stringa)-1:
            finished = True
            break
        a = stringa[i]
        b = stringa[i+1]
        if (a.lower() == b.lower()) and ((a.isupper() and b.islower()) or (a.islower() and b.isupper())):
            hasunits = True
            finished = True
        i += 1
    return hasunits

def collapse(stringa):
    stringa = string_to_list(stringa)
    i = 0
    finished = False
    while finished == False:
        if i == len(stringa)-1:
            finished = True
            break
        a = stringa[i]
        b = stringa[i+1]
        if (a.lower() == b.lower()) and ((a.isupper() and b.islower()) or (a.islower() and b.isupper())): #se aA o Aa
            stringa.pop(i)
            stringa.pop(i)
            i -= 3
            if i < 0:
                i = 0
            # print(list_to_string(input))
        i += 1
        if i == len(stringa)-1:
            finished = True
    stringa=list_to_string(stringa)
    return stringa
    
while HasUnits(mystring) == True:
    mystring = collapse(mystring)
soluzione1 = len(mystring)
# print(mystring)

# soluzione1 = "UNKNOWN"
# soluzione1 = len(input)

print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 
print()

alphabet = "abcdefghijklmnopqrstuvwxyz"
lenghts = []

for c in alphabet:
    replace1 = str(c)
    replace2 = str(c.upper())
    # print(replace1)
    # print(replace2)
    newstring = mystring.replace(replace1, '')
    newnewstring = newstring.replace(replace2,'')
    
    while HasUnits(newnewstring) == True:
        newnewstring = collapse(newnewstring)
    lunghezza = len(newnewstring)
    lenghts.append((lunghezza,c))
    # print(newnewstring)
    # print(lenghts)


lenghts.sort()
# print(lenghts[0][0])
soluzione2 = "UNKNOWN"
soluzione2 = lenghts[0][0]

print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




