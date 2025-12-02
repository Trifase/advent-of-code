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



ship = [0,0]
wp = [10,1]

def movewp(dir,num):
    global wp
    num = int(num)
    if dir in ["E", "W"]:
        if dir == "E":
            wp[0] += num
        elif dir == "W":
            wp[0] -= num
    if dir in ["N", "S"]:
        if dir == "N":
            wp[1] += num
        elif dir == "S":
            wp[1] -= num
    
    pass

def rotate(lr,n):                   # wp = [10,2]
    global wp
    steps = int(int(n)/90)
    if lr == "L":               #CCW
        for i in range(steps):
            wp = [-wp[1], wp[0]]    # wp = [-2,10]
    else:                       #CW
        for i in range(steps):
            wp = [wp[1], -wp[0]]    # wp = [2,-10]
    
      
    

def forward(dir,num):
    global ship
    global wp
    num = int(num)
    ship = [ship[0]+(wp[0]*num), ship[1]+(wp[1]*num)]
    #wp = [ship[0]+wp[0], ship[1]+wp[1]]
    pass

for i in lines:
    cosa = i[:1]
    quantita = i[1:]
    if cosa in ["E","S","W","N"]:
        print(f'{lines.index(i)}: {cosa}{quantita} - MOVE THE WAYPOINT!')
        movewp(cosa, quantita)
    elif cosa in ['L', 'R']:
        print(f'{lines.index(i)}: {cosa}{quantita} - ROTATE THE WAYPOINT!')
        rotate(cosa, quantita)
    elif cosa == 'F':
        print(f'{lines.index(i)}: {cosa}{quantita} - FORWARD!')
        forward(cosa, quantita)
    else:
        print(f"ALT! Non so che istruzione è: {i}")

    print(f'Posizione nave:{ship}\tPosizione Waypoint:{wp}')
print(f'{Fore.RED}Soluzione Parte 2: [{abs(ship[0])+abs(ship[1])}]')    

    

