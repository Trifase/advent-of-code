import re
# from rich import print
import copy
from typing import NewType, final
from aoc import get_input
import statistics, math, random
import logging
import time
from PIL import Image, ImageDraw 
from collections import Counter, defaultdict

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

def bin_to_dec(string, bit=2):
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

DAY = 16
TEST = 0


if TEST:
    FILENAME = f"inputs/{DAY:02d}-test.txt"
else:
    FILENAME = f"inputs/{DAY:02d}.txt"

level = logging.INFO
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)
start_time = time.perf_counter()

# Parsing
input = [l.strip() for l in open(FILENAME).readlines()]


def hex_to_binary_4_bits(string):
    binary = ''.join(format(int(x, 16), '04b') for x in string)
    return binary

sol1 = 0
versions = []
cursor = 0
string = input[0]
def parse_packet(string):
    global cursor
    print(f"\nParsing packet: {string}")

    version = binstring[cursor:cursor + 3].zfill(4)
    cursor += 3 
    versions.append(bin_to_dec(version))
    type_id = binstring[cursor:cursor + 3].zfill(4)
    cursor += 3

    print(f"Version: {version} [{bin_to_dec(version,2)}]\nType: {type_id} [{bin_to_dec(type_id,2)}]")

    if bin_to_dec(type_id) == 4:  # literal
        last_group_found = False
        literal = ""
        while last_group_found == False:
                group = binstring[cursor:cursor + 5]
                if group[0] == '0':
                    last_group_found = True
                    literal += group[1:]
                    print(f"{group[0]} {group[1:]} - [{literal}] [LAST]")
                    cursor += 5
                else:
                    cursor += 5
                    literal += group[1:]
        print(f"Literal: {literal} [{bin_to_dec(literal)}]")
        return bin_to_dec(literal)

    else:  # operator
        values = []
        typeid = copy.copy(bin_to_dec(type_id))
        length_type_id = binstring[cursor:cursor + 1]
        cursor += 1
        print(f"Length type: [{length_type_id}] ", end="")

        if length_type_id == "0":  # total length (next 15 bits)
            length = binstring[cursor:cursor + 15]
            n = bin_to_dec(length)
            print(f"Lenght in bits: {n}")
            cursor += 15
            packets_end = cursor + n
            while cursor < packets_end:
                values.append(parse_packet(binstring[cursor:]))

        else:  # number of sub packets (11 bits) 
            length = binstring[cursor:cursor + 11]
            print(f"Number of sub-packets: {bin_to_dec(length)}")
            cursor += 11
            n = bin_to_dec(length)
            for i in range(n):
                print(f"parsing packet: {i + 1}/{n}")
                values.append(parse_packet(binstring[cursor:]))
    
    if typeid == 0:
        return sum(values)
    elif typeid == 1:
        return math.prod(values)
    elif typeid == 2:
        return min(values)
    elif typeid == 3:
        return max(values)
    elif typeid == 5:
        return 1 if values[0] > values[1] else 0
    elif typeid == 6:
        return 1 if values[0] < values[1] else 0
    elif typeid == 7:
        return 1 if values[0] == values[1] else 0



    
string = input[0]
# string = "9C0141080250320F1802104A08"
print(f"Parsing packet: {string}")
binstring = hex_to_binary_4_bits(string)


sol2 = parse_packet(binstring)
# print(f"Versions: {versions} - Sum {sum(versions)} Len")

sol1 = sum(versions)
# Part 2

if TEST:
    print("\n\n====================\nTesting environment:\n====================")
print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")



