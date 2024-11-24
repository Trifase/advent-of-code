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
    lista = [ c for c in string ]
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

day = 4
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
print()
log = []
for line in lines:
    timestamp,year,month,day,hour,minute,action = rematch(r"\[(([\d]+)-([\d]+)-([\d]+) ([\d]+):([\d]+))\] (.+)", line).groups()
    log.append([timestamp,month,day,hour,minute,action])
log.sort()
# pp.pprint(log)

# sleeptime = {}
# guards = {}
#{ guardia: {data: sleep, data:sleep}}
#{ 10: {10-02: '24-42',10-03: }
#oppure
#{data:[(guardia, sleepin, sleepout), (guardia, sleepin, sleepout)]} forse così è meglio
# guardie = {}
# oggi = []
# events = [] #lista
events = {} #dict
oggi = []
guardia = 0
SleepIn = 0
SleepOut = 0
for event in log:

    # guardset = False
    # newguard = False
    # day = 0
    # lastday = 0
    # newday = False
    SleepBegin = False
    SleepEnd = False
    month = event[1]
    day = event[2]
    action = event[5]
    minutes = event[4]

    if action.startswith('G'): #guardia begins
        tempaction = action.split()
        # guardset = True
        guardia = tempaction[1][1:] #10
    if action.startswith('f'): #asleep
        SleepBegin = True
        SleepIn = int(minutes) #25
    if action.startswith('w'): #wakeup
        SleepOut = int(minutes) # 55
        SleepEnd = True
    if SleepEnd == True:
        # events.append((guardia,SleepIn,SleepOut)) #lista
        if guardia not in events:
            templist = []
        else:
            templist = events[guardia]
        templist.append((SleepIn,SleepOut))
        events[guardia] = templist
        SleepEnd = False

# print(events)
def HowMuchSleep(guardia):
    lista = events[guardia]
    sleep = 0
    for i in lista:
        sleep += i[1]-i[0]
    return sleep

# pp.pprint(events)
maxminuti = []

#Per ogni guardia, quanto ha dormito?

for guardia in events: 
    minuti = HowMuchSleep(guardia)
    maxminuti.append((guardia,minuti))
    # print(f'Guardia #{guardia} ha dormito {minuti} minuti.')

MostSleepy = sorted(maxminuti, key = lambda i: i[1], reverse = True)[0][0]

print(f'La guardia che ha dormito di più è: #{MostSleepy}')
# for guardia,inizio,fine in events:
#     print(f'{guardia}: {inizio}-{fine}\tTot:{int(fine)-int(inizio)}')


def MostCommonMinute(guardia):
    allminutes = range(0,60)
    tempdict = {}
    for m in allminutes:
        tempdict[m] = 0
    for breaks in events[guardia]:
        tempset=set(i for i in range(breaks[0],breaks[1]))
        for m in tempset:
            tempdict[m] += 1
    max_key = max(tempdict, key=tempdict.get)
    return int(max_key)

def expand(intervallo):
    temp = set(i for i in range(intervallo[0],intervallo[1]))
    return temp

mostfrequentminute = MostCommonMinute(MostSleepy)
print(f'Il minuto più frequente della guardia #{MostSleepy} è il minuto {mostfrequentminute}.')



# soluzione1 = "UNKNOWN"
soluzione1 = mostfrequentminute*int(MostSleepy)
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{soluzione1}]') 
print()

# print(f'Events: {events}')
# listaminutiperguardia = []
# for guardia in events:
#     listabreak = events[guardia]
#     setespanso = set()
#     for intervallo in listabreak:
#         setespanso = setespanso.union(expand(intervallo))
#     listaminutiperguardia.append((guardia,setespanso))
# print(listaminutiperguardia)

# [('10', {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54}), ('99', {36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54})]

# for tupla in listaminutiperguardia:
# allminutes = range(0,60)
# tempdict = {}
# for m in allminutes:
#     tempdict[m] = 0
# for tupla in listaminutiperguardia:
#     if m in i for i in tupla[1]: 
#             tempdict[m] += 1
# max_key = max(tempdict, key=tempdict.get)

# print(f'Events = {events}')
# print()
minuti_blank = {}
allminutes = range(0,60)
for m in allminutes:
    minuti_blank[m] = 0 
# for m in range(0,60):
#     numeri[m] = [(' ',0)]
# print(f'Minuti = {minuti}')

def minutidormiti(guardia):
    minuti = minuti_blank.copy()
    for intervallo in events[guardia]:
        ExpandedInterval= expand(intervallo) 
        for m in ExpandedInterval:
            minuti[m] += 1
    maxminute = max(minuti, key=minuti.get)
    all_values = minuti.values()
    maxvalue = max(all_values)
    return maxminute,maxvalue
     



topminuti = []
for guardia in events:
    minuto,quanti = minutidormiti(guardia)
    topminuti.append((quanti,minuto,guardia))
topminuti.sort(reverse=True)
# pp.pprint(topminuti)
print(f'Il vincitore è la guardia #{topminuti[0][2]}, che ha dormito al minuto {topminuti[0][1]} ben {topminuti[0][0]} volte!! ')
    
    # for intervallo in events[guardia]:
#         ExpandedInterval= expand(intervallo)
#         print(f'ExpandedInterval = {ExpandedInterval}')
        
#         # for m in minuti:
#         #     if m in intervallo:
#         #         minuticounter += 1
#         #     [m] = (guardia, counter)
# print(numeri)

            
        






soluzione2 = "UNKNOWN"
soluzione2 = int(topminuti[0][2])*topminuti[0][1]
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{soluzione2}]') 




