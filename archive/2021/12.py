import re
# from rich import print
import copy
from aoc import get_input
import statistics, math, random
import logging
import time
from PIL import Image, ImageDraw 
from collections import Counter

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

DAY = 12
TEST = 0

level = logging.INFO
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)
start_time = time.perf_counter()

# Parsing
if TEST:
    FILENAME = f"inputs/{DAY:02d}-test.txt"
else:
    FILENAME = f"inputs/{DAY:02d}.txt"

input = [l.strip() for l in open(FILENAME).readlines()]
caves = {}
for l in input:
    partenza, destinazione = l.split("-")
    # print(partenza, "->", destinazione)

    templist = caves.get(partenza, set())
    templist.add(destinazione)
    caves[partenza] = templist

    templist = caves.get(destinazione, set())
    templist.add(partenza)
    caves[destinazione] = templist



def DFS(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end:
        paths.append(path)
        # print(path)
    for node in graph[start]:
        if node.islower():
            if node not in path:
                DFS(graph, node, end, path)
        else:
            DFS(graph, node, end, path)


def DFS2(graph, start, end, path=[]):
    path = path + [start] 

    if start == end:
        # print(f"===Finito: {path}")
        paths2.append(path)
    if start not in ["end"]:
        for node in graph[start]:
            # print(f"{start}->{node}: {path}: ", end="")
            if node.isupper():
                # print(f"[{node}] è maiuscolo, avanti tutta")
                DFS2(graph, node, end, path)

            else:
                # print(f"[{node}] è minuscolo: ", end='')
                if node not in path:  # non ci siamo mai passati
                    # print("non ci siamo mai passati.")
                    DFS2(graph, node, end, path)

                else:  # ci siamo passati
                    # print("ci siamo già passati: ", end="")
                    if node in ["start", "end"]:
                        # print(f"non possiamo più andarci ripassarci perché è start o end")
                        pass

                    elif Counter([x for x in path if x.islower()]).most_common(1)[0][1] < 2:
                        # print(f"Possiamo ripassarci perché [nodo] è {Counter(path)[node]} - most_common è {Counter([x for x in path if x.islower()]).most_common(1)[0]}")
                        DFS2(graph, node, end, path)
                    else: 
                        pass
                        # print(f"non possiamo più andarci ripassarci perché c[{node}] è {Counter(path)[node]} - most_common è {Counter(path).most_common(1)[0]}")


# Part 1
sol1 = 0
paths = []

DFS(caves, "start", "end")

sol1 = len(paths)

print(f"Parte 1: \t[{sol1}]\n=======\n")


# Part 2
sol2 = 0
paths2 = []

DFS2(caves, "start", "end")

sol2 = len(paths2)


print(f"Parte 1: \t[{sol1}]\n")
print(f"Parte 2: \t[{sol2}]")
print(f"\nFinito in: {time.perf_counter()- start_time}")
