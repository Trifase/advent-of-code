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

day = 6
test = 0

# Parsing
if test == 1:
    FILENAME = f"{day}-test.txt"
else:
    FILENAME = f"{day}.txt"

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono
    # input = lines[0].split(",") #una nuova lista degli elementi splittati
    # lines = [int(n) for n in lines] #converte tutta la lista in int
# print(lines)

centers = []
print()
for line in lines:
    coord = line.split(",")
    centers.append((int(coord[0]),int(coord[1][1:])))
# print(f'Centers: {centers}')
# print(input)

def rettangolone(lista_centers,margine=1,shape=False): #ritorna una lista con due tuple, angolo alto a sx e angolo in basso a dx - se full=True ritorna una lista con tutti i punti del rettangolo. margine configurabile, default 1
    listax = [coord[0] for coord in lista_centers]
    listay = [coord[1] for coord in lista_centers]
    rect_coord = []
    rect_coord.append((min(listax)-margine,min(listay)-margine))
    rect_coord.append((max(listax)+margine,max(listay)+margine))
    if shape == False:
        return rect_coord
    rect_points = []
    for x in range (min(listax)-margine, max(listax)+margine):
        for y in range(min(listay)-margine, max(listay)+margine):
            rect_points.append((x,y))
    if shape == 'full':
        return rect_points
    for i in rettangolone(lista_centers,margine-1,shape='full'):
        if i in rect_points:
            rect_points.remove(i)
    if shape == 'borders':
        return rect_points

def manhattan(origin, dest):
    #The Manhattan Distance between two points (X1, Y1) and (X2, Y2) is given by |X1 – X2| + |Y1 – Y2|.
    return abs(origin[0]-dest[0])+abs(origin[1]-dest[1])


# print(rettangolone(centers)) #(0,0) (9,10) margine default = 1
# print(rettangolone(centers,2)) #(-1,-1) (10,11) perché margine = 2
# print(f"Punti: {rettangolone(centers,1,'full')}") #Tutti i punti tra -1,-1 e 10,11: 132 punti
# print(f"Bordi: {rettangolone(centers,1,'borders')}") #Solo i punti nei bordi, equivalente di rettangolone meno rettangolone con margine -1
listamanhattans = {}
templist = []
c = 0
for point in rettangolone(centers,1,'full'):
    distance_from_centers = []
    for center in centers:
        distance = manhattan(point,center)
        distance_from_centers.append((distance,center))
    distance_from_centers.sort()
    piuvicino = distance_from_centers[0] #(distance,center)
    quasipiuvicino = distance_from_centers[1]  #(distance,center)
    # print(distance_from_centers)
    if piuvicino[0] == quasipiuvicino[0]:   #se equidistante a due centri, lo dobbiamo ignorare
        # print(f'Il punto {point} è equidistante a due o più centri. Ignorato')
        c += 1
        continue #vai al prossimo punto
    centro,distanza = piuvicino[1],piuvicino[0]
    templist.append((point,centro,distanza))
    # print(f'Il punto {point} appartiene all\'area di {centro} a una distanza di {distanza}')
# print(templist) #punto, centro, distanza - (x,y), (x,y), n

for i in centers: # (8,9)
    listacentri = [] 
    for n in templist: # (1, 3), (8, 9), 0
        if i == n[1]:
            listacentri.append(n[0]) # (1,3)
    listamanhattans[i] = listacentri
print()
# pp.pprint(listamanhattans) #{centro: [(punto),(punto)]}
# print(rettangolone(centers,1,'borders'))
# print(bordi)

centrifiniti = {}
bordi = rettangolone(centers,1,'borders')
# print(bordi)
for centro in listamanhattans:
    infinito = False
    # print(f'controllo:\t{centro}\t{listamanhattans[centro]}',end=": ")
    print(f'controllo: {centro}',end=": ")
    for i in listamanhattans[centro]:
        if i in bordi:
            infinito = True
        
    if infinito == False:
        centrifiniti[centro] = listamanhattans[centro]
        print(f"{Fore.YELLOW}FINITO")
    else:
        print(f"{Fore.RED}INFINITO")
print()
# for i in centrifiniti:
#     print(f'{i}: {centrifiniti[i]}: {len(centrifiniti[i])}')

soluzione1 = "UNKNOWN"
soluzione1 = max(len(centrifiniti[i]) for i in centrifiniti)

print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 
print()

soluzione2 = "UNKNOWN"

griglia = rettangolone(centers,0,'full')
regioneinteressata = set()

for point in griglia:
    distances = []
    for center in centers:
        distances.append(manhattan(point,center))
    # if sum(distances) < 32: #test
    if sum(distances) < 10000: 
        regioneinteressata.add(point)



soluzione2 = len(regioneinteressata)

print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




