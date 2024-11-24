import re
from rich import print
import copy
from PIL import Image

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

def lista(lista):
    for i in lista:
        print(i)

def list_to_string(lista):
    string = ''.join(str(x) for x in lista)
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

def list_replace(lst, old="1", new="10"):
    """replace list elements (inplace)"""
    i = -1
    try:
        while 1:
            i = lst.index(old, i + 1)
            lst[i] = new
    except ValueError:
        pass

# Parsing

FILENAME = "inputs/06.txt"
# FILENAME = "inputs/06-test.txt"

lines = [l.strip() for l in open(FILENAME).readlines()]
fishes = [int(x) for x in lines[0].split(",")]

def cresci_pescetti(input_list: list[int], days: int, verbose: bool) -> int:
    fishes = input_list.copy()
    conteggio_pesci = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for eta in fishes:
        conteggio_pesci[eta] += 1

    for day in range(days):
        conteggio_pesci.append(conteggio_pesci.pop(0))
        conteggio_pesci[6] += conteggio_pesci[8]

        if verbose:
            print(f"Day {day+1}: {sum(conteggio_pesci)} pescetti.")

    return sum(conteggio_pesci)

sol1 = cresci_pescetti(fishes, 80, True)

print(f"Parte 1: \t[{sol1}]")


# Part 2
sol2 = cresci_pescetti(fishes, 256, True)

print(f"Parte 2: \t[{sol2}]")

