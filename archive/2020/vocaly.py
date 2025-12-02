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

FILENAME = "15.txt"
# FILENAME = "15-test.txt"

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

# Parsing

# stringa = input(str("Enter a word: ")).upper()
# for lettera in stringa:
#     if lettera in "AEIOU":
#         continue
#     else:
#         print(lettera)

c0 = int(input("Inserisci un numero:"))
while c0 != 1:
    if c0 % 2 == 0:
        print(c0/2)
        break
    else:
        print(3*c0+1)
        break