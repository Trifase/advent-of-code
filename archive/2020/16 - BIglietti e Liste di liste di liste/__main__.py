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

pp = pprint.PrettyPrinter(indent=3)

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

def lista(lista):
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

def removeduplicates(lista):
  return list(dict.fromkeys(lista))

# Parsing
FILENAME = "16.txt"                                                                                               #DAY16
# FILENAME = "16-test2.txt"                                                                                #TEST

with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono

def isinvalid(n):
    global regole
    for key in regole:
        if int(n) in regole[key]:
            return False
    else:
        return True


k = 0
binvalidi = []
regole = {}
listainvalidi = []
listavalidi = []
listafields = []
bigliettoinvalido = False
for i in range(len(lines)):
    if 0 <= i < 20: #regole                                                                                   #DAY16
    # if 0 <= i < 3: #regole-test                                                                         #TEST
        f, range1, range2 = rematch(r"(\D+): (\d+-\d+)\D+(\d+-\d+)", lines[i]).groups()
        field = f.replace(" ","_")
        r1 = range1.split("-")
        r2 = range2.split("-")
        regole[field] = list(range(int(r1[0]),int(r1[1])+1)) + list(range(int(r2[0]),int(r2[1])+1))
        print(f'[{range1} e {range2}] \tlen: {len(regole[field])} = {field}') #output solo per leggibilità
        # print(f'{field}=\tlen: {len(regole[field])}\t{regole[field]} ') #esteso, stampa la vera lista
    elif 25 <= i <= 259: 
        k += 1 #mi conto i biglietti, tanto per.
        #biglietti                                                                             #DAY16
    # elif 7 < i < 11: #biglietti-test                                                                    #TEST
        biglietto = lines[i].split(",") # biglietto = [nnn,nnn,nn,nnnn,nn,nn,nn]
        for n in biglietto:
            if isinvalid(n) is True: #se un valore non va in nessuna regola
                listainvalidi.append(int(n))  #aggiungo valore a lista listainvalidi
                bigliettoinvalido = True #setto booleano a caso
                break
        else:   #se non ci sono valori invalidi
            bigliettoinvalido = False #automaticamente il biglietto è valido
            
        if bigliettoinvalido == True: #se il biglietto è invalido
            binvalidi.append(biglietto) #aggiungo alla lista di biglietti invalidi binvalidi
        else:
            listavalidi.append(biglietto) #altrimenti aggiungo alla lista di biglietti validi listavaliri

        
    elif i == 22: #il tuo biglietto
        myticket = lines[i].split(",")
# print(regole)
print()
print(f'{Fore.RED}La soluzione alla parte 1 è: {Fore.GREEN}[{sum(listainvalidi)}]') #expected: # 436
print()
print(f'Numero di regole: {len(regole)}')
print(f'Numeri di parametri in un biglietto: {len(listavalidi[0])}') #un biglietto a caso
print(f'Numeri di biglietti non validi (da valori che etc, parte 1): {len(listainvalidi)}')
print(f'{listainvalidi}')
print(f'Numeri di biglietti non validi (da lista biglietti): {len(binvalidi)}')
print(f'Numero dei biglietti validi: {len(listavalidi)}')
print(f'Numeri di biglietti totali: {k}')

print()

# print("  [0]    [1]    [2]    [3]    [4]    [5]    [6]    [7]    [8]    [9]    [10]   [11]   [12]   [13]   [14]   [15]   [16]   [17]   [18]   [19]")
for i in listavalidi:
    print(i)
# print(f'Lista dei numeri invalidi: {listainvalidi}')


for i in range(len(listavalidi[0])): 
    templist = []
    for c in listavalidi:
        templist.append(int(c[i]))
    
    listafields.append(templist)
# lista(listafields)
associazioni = {}

print()
t = len(regole.keys())
k = 0
# print(t)
while t != 0:
    for param in range(len(listafields)):
        for field in regole:
            valori = set(listafields[param])
            regola = set(regole[field])
            # print(f'confronto {valori} con {regola}', end=": ")
            # print(f'confronto i valori alla posizione [{param}] con il campo {field}', end=": ")
            if valori.issubset(regola) == True:
                # print(f'{Fore.GREEN}Uè! Lista {param} è un subset di {field}') 
                fieldscelto = field
                k += 1
            else: 
                # print(f"{Fore.RED} Non ci sta") 
                pass
        # print(f"Finito ciclo 1: k = {k}")
        
        if k == 1: #se entra solo in una regola
            associazioni[str(fieldscelto)] =  param
            regole.pop(fieldscelto)
            t = len(regole.keys())
            k = 0
            print(f'Associato {param} con {fieldscelto}: ne mancano {t}')
        else:
            k = 0

pp.pprint(associazioni)
myindexes = [i for key, i in associazioni.items() if 'departure' in key.lower()]
print(f'Indici con "departure": {myindexes}')
print(f'Il mio biglietto": {myticket}')
temp = []
for index in myindexes:
    temp.append(int(myticket[index]))
print(f'I numeri che ci servono nel mio biglietto sono: {temp}')
print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{math.prod(temp)}]') #expected: # 436
