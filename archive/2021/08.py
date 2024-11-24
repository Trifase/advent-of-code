import re
from rich import print
import copy
from aoc import get_input
import statistics, math


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


def get_key_from_value(my_dict, to_find):
    for k,v in my_dict.items():
        if sorted(v) == sorted(to_find): return k
    return None

DAY = 8
TEST = 0


# Parsing
if TEST:
    FILENAME = f"inputs/{DAY:02d}-test.txt"
else:
    FILENAME = f"inputs/{DAY:02d}.txt"

FILENAME = f"inputs/8-100000.in"


def decode_pattern(pattern: list[str], digits: list[str], verbose: bool) -> int:

    decodifica = {}
    caratteri = "abcdefg"
    indice = {}.fromkeys(caratteri, 0)
    for c in (e for e in list_to_string(pattern) if e in indice):
        indice[c] += 1 
    decodemap = {}
    for string in pattern:
        # Entità conosciute: 1 (len(2)), 4 (len(4)), 7 (len(3)), 8 (len(7))
        if len(string) == 2:
            decodifica[1] = string
        elif len(string) == 4:
            decodifica[4] = string
        elif len(string) == 3:
            decodifica[7] = string
        elif len(string) == 7:
            decodifica[8] = string
        # A questo punto conosciamo i pattern per 1, 4, 7, 8. Ci mancano 0, 2, 3, 5, 6, 9, che hanno len(6) e len(5)
    for lettera, conteggio in indice.items():
        if conteggio == 4:
            decodemap["d_sx"] = lettera
        if conteggio == 6:
            decodemap["u_sx"] = lettera
        if conteggio == 9:
            decodemap["d_dx"] = lettera

        if conteggio == 8:
            if lettera in decodifica[4]:
                decodemap["u_dx"] = lettera
            else:
                decodemap["u"] = lettera

        if conteggio == 7:
            if lettera in decodifica[4]:
                decodemap["center"] = lettera
            else:
                decodemap["d"] = lettera
        
    for string in pattern:
        if len(string) in [2, 4, 3, 7]:
            continue
        elif len(string) == 5:  # 2, 3, 5
            if decodemap["d_sx"] in string:  # è un 2
                decodifica[2] = string
            elif decodemap["u_dx"] in string:  # è un 3
                decodifica[3] = string
            else:  # è un 5
                decodifica[5] = string
        elif len(string) == 6:  # 0, 6, 9
            if decodemap["center"] in string:  # non è uno 0
                if decodemap["d_sx"] in string:  # è un 6
                    decodifica[6] = string
                else:  # è un 9
                    decodifica[9] = string
            else:
                decodifica[0] = string
    digits_decodificato = [get_key_from_value(decodifica, x) for x in digits]
    if verbose:
        print(f"Decoded map: {decodifica}")
        print(f"Decoded digits: {digits_decodificato}")
        print(f"Decoded number: {int(list_to_string(digits_decodificato))}")
    return int(list_to_string(digits_decodificato))


lines = [l.strip() for l in open(FILENAME).readlines()]
tot = 0
sum = 0
import time
origin = time.perf_counter()
for l in lines:
    decode = l.split(" | ")[0].split()
    digits = l.split(" | ")[1].split()
    # print(f"Map: {decode} Digits to decode: {digits}")
    sum += decode_pattern(decode, digits, False)
    # print(f"{' '.join(digits)}: {decode_pattern(decode, digits, True)}")
    for d in digits:
        if len(d) in [2, 4, 3, 7]:
            tot += 1
    # decode_pattern(decode, digits)
    # print()
# print(f"==================\n         Tot: {sum}")




# Part 1
sol1 = tot
print(f"Parte 1: \t[{sol1}]\n")

# Part 2
sol2 = 0
sol2 = sum
print(f"Parte 2: \t[{sol2}]")
now = time.perf_counter()
print("time passed: ", now - origin)
