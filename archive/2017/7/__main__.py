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

day = 7
test = 1

# Parsing
if test == 1:
    FILENAME = f"{day}-test.txt"
else:
    FILENAME = f"{day}.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono
    # input = lines[0].split("\t") #una nuova lista degli elementi splittati
    # lines = [int(n) for n in lines] #converte tutta la lista in int
    # lines = [int(i) for i in input]
# print(lines)
# lines = ['fwft (72) -> ktlj, cntj, xhth', 'padx (45) -> pbga, havc, qoyq', 'tknk (41) -> ugml, padx, fwft']
tree = []

# def find_bottom(tree):
#     for x in tree and x['has_children'] == True:
#         print x['name']
#             for y in tree:
#                 if y['has_children']:
#                     if x['name'] not in y['children']:
#                         return x['name']
#     return "No bottom Found"


completree = []
for line in lines:
    father, weight, children = rematch(r"(.+) \((\d+)\)(?: \-\> (.+))?", line).groups()
    tempdict = {}
    tempdict["name"] = father
    tempdict["weight"] = int(weight)
    if children:
        tempdict["has_children"] = True
        tempdict["children"] = children.split(", ")
    else:
        tempdict["has_children"] = False
    completree.append(tempdict)


for line in lines:
    father, weight, children = rematch(r"(.+) \((\d+)\)(?: \-\> (.+))?", line).groups()
    # tempdict = {}
    # tempdict["name"] = father
    # tempdict["weight"] = int(weight)
    if children:
        for i in children.split(", "):
            tree.append((father,i))
        # tempdict["has_children"] = True
        # tempdict["children"] = children.split(", ")
    # else:
        # tempdict["has_children"] = False
    # tree.append(tempdict)

def find_first_node(edges): #return the node with no fathers
    lista = [i[1] for i in edges]
    first_node_found = False
    for edge in edges:
        if edge[0] not in lista:
            first_node_found = True
            return edge[0]

def getweight(name,):
    for node in completree:
        if node['name'] != name:
            continue    
        else:
            return node['weight']

def is_balanced(software):
    for node in completree:
        if node['name'] != software:
            continue    
        else:
            if node['has_children'] == False:
                return "Non ha figli"
            else:   
                templist = []
                for child in node['children']:
                    templist.append(getweight(child))
                if sum(templist)//len(templist) == templist[0]:
                    return True
                else:
                    return False
                


print(tree)
pp.pprint(completree)
print("---")
first = find_first_node(tree)
print(is_balanced(first))
# print(find_first_node(tree))

# print(find_bottom(tree))
# for x in tree and x['has_children'] == True:
    # print(x['name'])

print()
soluzione1 = "UNKNOWN"
soluzione1 = find_first_node(tree)
# 
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 
print("----")
soluzione2 = soluzione1
# soluzione2 = steps-last_ID-1
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




