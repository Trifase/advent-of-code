import itertools
import math
import os
import re
import sys
from collections import defaultdict
from functools import partial
from typing import Dict, List, Tuple
import pprint
from colorama import init, Fore, Back

init()

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

with open("12.txt") as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono

card = ["E","S","W","N"]
head = "E"
pos_h = 0
pos_v = 0

def move(dir,num):
    global pos_h
    global pos_v
    num = int(num)
    if dir in ["E", "W"]:
        if dir == "E":
            pos_h += num
        elif dir == "W":
            pos_h -= num
    if dir in ["N", "S"]:
        if dir == "N":
            pos_v += num
        elif dir == "S":
            pos_v -= num
    
    pass

def rotate(lr,n):
    n = int(n)
    steps = n/90
    global head
    global cosa
    global quantita
    if lr == "L":
        steps = steps*-1
        print(f'{Fore.GREEN}Ruoto a sinistra [{abs(int(steps))}] volte{Fore.WHITE}', end=" e ", flush=True)
    else:
        print(f'{Fore.GREEN}Ruoto a destra [{abs(int(steps))}] volte{Fore.WHITE}', end=" e ", flush=True)
    oldhead = card.index(head)
    newhead = int(oldhead + steps)%4
    # print
    # print(newhead)
    # print(newhead%4)
    print(f'vado da [{head}] a [{card[newhead]}]')
    head = card[newhead%4]
    
    

def forward(dir,num):
    global head
    global head
    move(head,num)
    pass

for i in lines:
    cosa = i[:1]
    quantita = i[1:]
    if cosa in ["E","S","W","N"]:
        print(f'{lines.index(i)}: {cosa}{quantita} - MOVE!')
        move(cosa, quantita)
    elif cosa in ['L', 'R']:
        print(f'{lines.index(i)}: {cosa}{quantita} - ROTATE!', end=" ", flush=True)
        rotate(cosa, quantita)
    elif cosa == 'F':
        print(f'{lines.index(i)}: {cosa}{quantita} - FORWARD!')
        forward(cosa, quantita)
    else:
        print(f"ALT! Non so che istruzione è: {i}")

    print(f'Siamo a E: {pos_h} e N:{pos_v}')
print(f'{Fore.RED}Soluzione Parte 1: [{abs(pos_h)+abs(pos_v)}]')    

    

