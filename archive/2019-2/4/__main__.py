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

day = 4
test = 0

# Parsing
if test == 1:
    FILENAME = f"{day}-test.txt"
else:
    FILENAME = f"{day}.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono
    ranges = lines[0].split("-")
    ranges = [int(n) for n in ranges]

#Begin

def hasDoubleDigit(password): #123445 OK - #123456 NO
    for n in password:
        # if password.count(n) > 1: #part 1 #124445 OK - #123456 NO
        if password.count(n) == 2: #part 2  #124445 NO - #111144 SI
            return True
    return False

def neverDecrease(password): #111234 OK - #123454 NO
    for i in range(len(password)):
        if i == 0: 
            continue
        if password[i] < password[i-1]:
            return False
    return True

def isValid(password):
    if hasDoubleDigit(password):
        if neverDecrease(password):
            return True
    return False

counter = 0
# TESTLIST = [111111, 223450, 123789, 111123, 122345]
for password in range(ranges[0],ranges[1]): #158126-624574
    if isValid(str(password)):
        counter += 1

# part1
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{counter}]') 


# part 2
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{counter}]')