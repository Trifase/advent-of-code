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

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

# Parsing
with open("11.txt") as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una floor di tutte le righe così come sono

oldfloor = []
floor = []
floor2 = []
occupiedseats = 0
tick = 0

def aggiungibordo():
    global floor
    floor = ["."+line.strip()+"." for line in file]
    floor.insert(0,"."*len(floor[0]))
    floor.append("."*len(floor[1]))

def aggiungilimite():
    global floor
    floor = ["x"+line+"x" for line in floor]
    floor.insert(0,"x"*len(floor[0]))
    floor.append("x"*len(floor[1]))


def viewmap(lista):
    global floor
    global floor2
    print("   ", end="")
    for i in range(len(lista[0])):
        print(f'{str(i).zfill(2)}', end=" ")
    print()

    for index, i in enumerate(lista):
        print(f'{str(index).zfill(2)}', end="  ")
        for x in range(len(lista[index])):
            if lista[index][x] == "L":
                print(f'{Style.BRIGHT}{Fore.GREEN}{lista[index][x]}', end="  ")
            elif lista[index][x] == "#":
                print(f'{Fore.RED}{lista[index][x]}', end="  ")
            else:
                print(f'{Style.DIM}{lista[index][x]}', end="  ")
        print()

def checkseat(y,x):
    global floor
    occupied = 0
    # print(f'Conto i posti occupati intorno a ({y},{x})')
    for a in range(y-1,y+2):
        for b in range(x-1,x+2):
            # print(f'({a},{b}): [{floor[a][b]}]')
            if floor[a][b] == "#":
                if a == y and b == x:
                    # print("Questo è il nostro posto")
                    # print("^ We don't count this, è il nostro posto")
                    pass
                else:
                    occupied += 1
                # print(f"Occupato. Tot: {occupied}")
            
    return occupied

def checkvisibleoccupiedseat(y,x):
    global floor
    origin = (y,x)
    visibleoccupied = 0
    # print(f'Conto i posti visibili occupati intorno a ({y},{x})')
    checkedN = False
    checkedNE = False
    checkedE = False
    checkedSE = False
    checkedS = False
    checkedSW = False
    checkedW = False
    checkedNW = False
    while checkedN is False:
        # print(f'[N] Provo ({y},{x}):', end=" ")
        if floor[y-1][x] == "#": 
            visibleoccupied +=1
            checkedN = True
            # print(f"{Fore.RED}[N] Occupato!")
        elif floor[y-1][x] == ".":
            # print("[N] Libero!")
            y -= 1
        elif floor[y-1][x] == "L":
            checkedN = True
        else: #se è x
            # print(f"{Fore.YELLOW}[N] Ouch! Muro!")
            checkedN = True
    y = origin[0]
    x = origin[1]

    while checkedNE is False:
        # print(f'[NE] Provo ({y},{x}):', end=" ")
        if floor[y-1][x+1] == "#": 
            visibleoccupied +=1
            checkedNE = True
            # print(f"{Fore.RED}[NE] Occupato!")
        elif floor[y-1][x+1] == ".":
            # print("[NE] Libero!")
            y -= 1
            x += 1
        elif floor[y-1][x+1] == "L":
            checkedNE = True
        else: #se è x
            # print(f"{Fore.YELLOW}[NE] Ouch! Muro!")
            checkedNE = True
    y = origin[0]
    x = origin[1]

    while checkedE is False:
        # print(f'[E] Provo ({y},{x}):', end=" ")
        if floor[y][x+1] == "#": 
            visibleoccupied +=1
            checkedE = True
            # print(f"{Fore.RED}[E] Occupato!")
        elif floor[y][x+1] == ".":
            # print("[E] Libero!")
            x += 1
        elif floor[y][x+1] == "L":
            checkedE = True
        else: #se è x
            # print(f"{Fore.YELLOW}[E] Ouch! Muro!")
            checkedE = True
    y = origin[0]
    x = origin[1]

    while checkedSE is False:
        # print(f'[SE] Provo ({y},{x}):', end=" ")
        if floor[y+1][x+1] == "#": 
            visibleoccupied +=1
            checkedSE = True
            # print(f"{Fore.RED}[SE] Occupato!")
        elif floor[y+1][x+1] == ".":
            # print("[SE] Libero!")
            x += 1
            y += 1
        elif floor[y+1][x+1] == "L":
            checkedSE = True
        else: #se è x
            # print(f"{Fore.YELLOW}[SE] Ouch! Muro!")
            checkedSE = True
    y = origin[0]
    x = origin[1]

    while checkedS is False:
        # print(f'[S] Provo ({y},{x}):', end=" ")
        if floor[y+1][x] == "#": 
            visibleoccupied +=1
            checkedS = True
            # print(f"{Fore.RED}[S] Occupato!")
        elif floor[y+1][x] == ".":
            # print("[S] Libero!")
            y += 1
        elif floor[y+1][x] == "L":
            checkedS = True
        else: #se è x
            # print(f"{Fore.YELLOW}[S] Ouch! Muro!")
            checkedS = True
    y = origin[0]
    x = origin[1]

    while checkedSW is False:
        # print(f'[SW] Provo ({y},{x}):', end=" ")
        if floor[y+1][x-1] == "#": 
            visibleoccupied +=1
            checkedSW = True
            # print(f"{Fore.RED}[SW] Occupato!")
        elif floor[y+1][x-1] == ".":
            # print("[SW] Libero!")
            x -= 1
            y += 1
        elif floor[y+1][x-1] == "L":
            checkedSW = True
        else: #se è x
            # print(f"{Fore.YELLOW}[SW] Ouch! Muro!")
            checkedSW = True
    y = origin[0]
    x = origin[1]

    while checkedW is False:
        # print(f'[W] Provo ({y},{x}):', end=" ")
        if floor[y][x-1] == "#": 
            visibleoccupied +=1
            checkedW = True
            # print(f"{Fore.RED}[W] Occupato!")
        elif floor[y][x-1] == ".":
            # print("[W] Libero!")
            x -= 1
        elif floor[y][x-1] == "L":
            checkedW = True
        else: #se è x
            # print(f"{Fore.YELLOW}[W] Ouch! Muro!")
            checkedW = True
    y = origin[0]
    x = origin[1]

    while checkedNW is False:
        # print(f'[NW] Provo ({y},{x}):', end=" ")
        if floor[y-1][x-1] == "#": 
            visibleoccupied +=1
            checkedNW = True
            # print(f"{Fore.RED}[NW] Occupato!")
        elif floor[y-1][x-1] == ".":
            # print("[NW] Libero!")
            x -= 1
            y -= 1
        elif floor[y-1][x-1] == "L":
            checkedNW = True
        else: #se è x
            # print(f"{Fore.YELLOW}[NW] Ouch! Muro!")
            checkedNW = True
    y = origin[0]
    x = origin[1]


    return visibleoccupied

def contaoccupati(lista):
    occupiedseats = 0
    for i in lista:
        occupiedseats += i.count('#')
    return occupiedseats

def dofloor():
    global occupiedseats
    global oldfloor
    global tick
    global floor
    global floor2
    floor2 = []
    tick += 1
    # print(f'floor: {floor}') 
    # print(f'floor2: {floor2}') 
    # print()
    for y in range(len(floor)):
        templist = list(floor[y])
        tempstring = []
        # print(f'Riga numero {y} (prima): {floor[y]}')
        # print(f'Espando {y}: {templist}')
        
        for x in range(len(templist)):
            # print(f'({y},{x}) - [{floor[y][x]}]') #, end=": "
            if y == 0 or y == len(floor)-1 or x == 0 or x == len(floor[y])-1:
                # print("Bordo")
                tempstring.append(templist[x])
            else: 
                # print(f'[{floor[y][x]}] {checkseat(y,x)}', end=" ")
                if floor[y][x] == "L":
                    if checkseat(y,x) == 0:
                        tempstring.append(templist[x].replace("L","#"))
                    else: 
                        tempstring.append(templist[x])
                elif floor[y][x] == "#":
                    if checkseat(y,x) > 3:
                        tempstring.append(templist[x].replace("#","L"))
                    else: 
                        tempstring.append(templist[x])
                elif floor[y][x] == ".":
                    tempstring.append(templist[x])
        # print(f'tempstring: {tempstring}')
        tempstring2 = ''.join(tempstring)
        floor2.append(tempstring2)
        # print(f'floor2[y]: {floor2[y]}')    
        # print(f'floor2: {floor2}')
        # print(f'floor : {floor}')        
        # print()
    oldfloor = floor
    floor = floor2

            

            # if floor[y][x] == "L":
            #     print(checkseat(y,x))
            # elif floor[y][x] == "#" and checkseat(y,x) > 3:
            #     floor[y][x] == floor[y][x].replace("#","L")

def dofloor2():
    global occupiedseats
    global oldfloor
    global tick
    global floor
    global floor2
    floor2 = []
    tick += 1
    # print(f'floor: {floor}') 
    # print(f'floor2: {floor2}') 
    # print()
    for y in range(len(floor)):
        templist = list(floor[y])
        tempstring = []
        # print(f'Riga numero {y} (prima): {floor[y]}')
        # print(f'Espando {y}: {templist}')
        
        for x in range(len(templist)):
            # print(f'({y},{x}) - [{floor[y][x]}]') #, end=": "
            if y == 0 or y == len(floor)-1 or x == 0 or x == len(floor[y])-1:
                # print("Bordo")
                tempstring.append(templist[x])
            else: 
                # print(f'[{floor[y][x]}] {checkseat(y,x)}', end=" ")
                if floor[y][x] == "L":
                    if checkvisibleoccupiedseat(y,x) == 0:
                        tempstring.append(templist[x].replace("L","#"))
                    else: 
                        tempstring.append(templist[x])
                elif floor[y][x] == "#":
                    if checkvisibleoccupiedseat(y,x) > 4:
                        tempstring.append(templist[x].replace("#","L"))
                    else: 
                        tempstring.append(templist[x])
                elif floor[y][x] == ".":
                    tempstring.append(templist[x])
        # print(f'tempstring: {tempstring}')
        tempstring2 = ''.join(tempstring)
        floor2.append(tempstring2)
        # print(f'floor2[y]: {floor2[y]}')    
        # print(f'floor2: {floor2}')
        # print(f'floor : {floor}')        
        # print()
    oldfloor = floor
    floor = floor2

            

            # if floor[y][x] == "L":
            #     print(checkseat(y,x))
            # elif floor[y][x] == "#" and checkseat(y,x) > 3:
            #     floor[y][x] == floor[y][x].replace("#","L")

aggiungibordo()
aggiungilimite()
# print("")
# print("Stato iniziale:")
# viewmap(floor)
# print(f'Posti occupati: {contaoccupati(floor)}')
# print(f'Provo a vedere i posti occupati visibili a (4,7): {checkvisibleoccupiedseat(4,7)}')

print()
oldoccupati = 1
newoccupati = 12
while oldoccupati != newoccupati:
    oldoccupati = contaoccupati(floor)
    # dofloor()
    dofloor2()
    #viewmap(floor)
    print(f'Iterazione #{tick}\tPosti occupati: {contaoccupati(floor)}')
    print()
    newoccupati = contaoccupati(floor)
print(f'{Fore.RED}Fatto! Ci sono volute {tick} iterazioni, ma la gente si è fermata. I posti occupati sono [{newoccupati}].')

# dofloor()
# viewmap(floor)
# print(f'Posti occupati per (1,3) [exp: 4]: {checkseat(1,3)}')
# print(f'Posti occupati per (9,6) [exp: 8]: {checkseat(9,6)}')
# print(f'Posti occupati per (6,1) [exp: 1]: {checkseat(6,1)}')
# print()
# print(f'Floor = {floor}')
# print()
# print()









# print(f'{Fore.RED}Soluzione Parte 1: [{abs(pos_h)+abs(pos_v)}]')    

# BACKUP
# def dofloor(): 
#     global floor
#     global floor2
#     floor2 = []
#     print(f'floor: {floor}') 
#     print(f'floor2: {floor2}') 
#     print()
#     for y in range(len(floor)):
#         templist = list(floor[y])
#         tempstring = []
#         print(f'Riga numero {y} (prima): {floor[y]}')
#         print(f'Espando {y}: {templist}')
        
#         for x in range(len(templist)):
#             print(f'({y},{x}) - [{floor[y][x]}]') #, end=": "
#             if y == 0 or y == len(floor)-1 or x == 0 or x == len(floor[y])-1:
#                 print("Bordo")
#                 tempstring.append(templist[x])
#             else: 
#                 print(f'[{floor[y][x]}] {checkseat(y,x)}', end=" ")
#                 if floor[y][x] == "L":
#                     if checkseat(y,x) == 0:
#                         tempstring.append(templist[x].replace("L","#"))
#                     else: 
#                         tempstring.append(templist[x])
#                     #floor2.insert(x, templist[x].replace("L","#"))
#                     # print(f"Sedia {Fore.GREEN}libera{Fore.WHITE} con {checkseat(y,x)} persone attorno")
#                 elif floor[y][x] == "#":
#                     if checkseat(y,x) > 3:
#                         tempstring.append(templist[x].replace("#","L"))
#                     else: 
#                         tempstring.append(templist[x])
#                     # print(f"Sedia {Fore.RED}occupata{Fore.WHITE} con {checkseat(y,x)} persone attorno")
#                 elif floor[y][x] == ".":
#                     tempstring.append(templist[x])
#                     # print("Pavimento")
#         print(f'tempstring: {tempstring}')
#         tempstring2 = ''.join(tempstring)
#         floor2.append(tempstring2)
#         print(f'floor2[y]: {floor2[y]}')    
#         print(f'floor2: {floor2}')
#         print(f'floor : {floor}')        
#         print()
            

#             # if floor[y][x] == "L":
#             #     print(checkseat(y,x))
#             # elif floor[y][x] == "#" and checkseat(y,x) > 3:
#             #     floor[y][x] == floor[y][x].replace("#","L")
