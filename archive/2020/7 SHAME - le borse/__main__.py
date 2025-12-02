import itertools
import math
import os
import re
import sys
from collections import defaultdict
from functools import partial
from typing import Dict, List, Tuple
import pprint

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

with open("7.txt") as f:
    input = f.readlines()   
    lines = [line.strip() for line in input] #una lista di tutte le righe così come sono

#posso splittare tutto per CONTAIN così ho un colore a sx e uno o più colori a destra
#posso fare una funzione get_color e get_color_contain che mi restituisce in ordine un colore (via regex XXX XXX (bag|bags)) e una lista di colori (eventualmente coi numeri per la parte 2)
#posso farmi una set_colori coi colori univoci e poi contarlo

##alternativamente funzione can_contain_gold per ogni colore che restituisce true se quel colore (e i colori che contiene) possono contenere gold


# lines = [
#     'light teal bags contain 4 drab magenta bags, 2 dull crimson bags, 5 posh brown bags.',
#     'vibrant plum bags contain 6 dull crimson bags.'
#     ]
 
# allbags = {}
# bag = {}
# #parsing
# for line in lines:
#     color, regole = rematch(r"(.*) bags contain (.*).", line).groups() #regexp per matchare tutto ciò che c'è prima e dopo bags contain, e usare groups per farle diventare variabili color e rules
#     for regola in regole.split(", "): #per ogni regola, splittiamo i vari figli
#         if regola == "no other bags": #se la regola è che non hanno figli
#             continue # non facciamo niente
#         n, c = rematch(r"(\d+) (.*) bags?", regola).groups() #altrea regex che estrae il numero e il colore dalle regole
#         # print(f'color: {color} - CONTIENE:  n: {n} - c: {c}')
#         n = int(n)
#         bag[n] = c
#         # print(bag)
#     allbags[color] = bag
#     bag = {}

def wherebag(borsa):
    listacontenitori = []
    for k, v in allbags[borsa].items():
        listacontenitori.append(k)
    # for b in listacontenitori:
    #     if not wherebags[b]:
    #         return
    #     wherebag(b)
    print(listacontenitori)
    return len(listacontenitori)

def removeduplicates(lista):
  return list(dict.fromkeys(lista))



#parsing
allbags = {}
bag = {}
contaregole = 0
for line in lines:
    bag = {}
    contenitore, regole = rematch(r"(.*) bags contain (.*).", line).groups() #regexp per matchare tutto ciò che c'è prima e dopo bags contain, e usare groups per farle diventare variabili color e rules
    # print("###########################")
    print(f'NUOVA REGOLA: {line}')
    for regola in regole.split(", "): #per ogni regola, splittiamo i vari figli
        # print(f'CONTENITORE: {contenitore}')
        # print(f'ANALIZZO: {regola}')
        if regola == "no other bags": #se la regola è che non hanno figli
            continue # non facciamo niente
        n, contenuto = rematch(r"(\d+) (.*) bags?", regola).groups() #altrea regex che estrae il numero e il colore delle borse contenute
        # print(f'DENTRO: {contenitore}  CI SONO: {n} COSA: {contenuto}')
        contaregole += 1
        bag[contenuto] = n #bag["light teal"] = 5
        # print(f'PARTE DA AGGIUNGERE: {bag}')
        allbags[contenitore] = bag 
        # print(f'DIZIONARIO: {allbags}')
        # print("")             
print(f"\nFINE ANALISI REGOLE: trovate {contaregole} regole\n")
pp = pprint.PrettyPrinter(indent=3, compact=True, sort_dicts=False)
# pp.pprint(allbags)
dacercare = []
trovati = []
backupresults = []
borse = []
contaborse = 0 
nemancano = 1
print("cerco: shiny gold")
for i in allbags.items():
    if "shiny gold" in i[1]:
        dacercare.append(i[0])
        borse.append(i[0])
print(f'Prima ricerca: {dacercare}')
contaborse += len(dacercare)
nemancano = len(dacercare)
print(f"trovate: {nemancano}")
while nemancano != 0:
    # print(f'dacercare: {dacercare} trovati: {trovati} nemancano: {nemancano} contaborse: {contaborse}')
    for x in dacercare:
        print(f"cerco: {x}")
        for i in allbags.items():
            if x in i[1]:
                trovati.append(i[0])
                borse.append(i[0])
        print(trovati)
        contaborse += len(trovati)
        print(f"trovate: {len(trovati)} totale: {contaborse}")
        dacercare.remove(x)
    dacercare = trovati
    trovati = []
    
    nemancano = len(dacercare)

# print(contaborse)
# print(borse)
print ("rimuovo duplicati...")
borse = removeduplicates(borse)
# print(borse)
print(len(borse))

    
# print('DIZIONARIO - {"bag": {n1:"bag2", n2:"bag2"}}')
# print("")
#print(wherebags)
#WHEREBAGS = {BORSA CONTENUTA IN: {BORSA: QUANTITA}}
# print("")
#wherebag("dull crimson")

# print('Soluzione che devo tirare fuori: ["bright white", "muted yellow", "light red", "dark orange"]')
# print('wherebags = {"drab magenta":{"light teal": 4}, "dull crimson": {"light teal": 2, "vibrant plum": 5}, "posh brown":{"light teal": 3}}')
#print('wherebags = {"drab magenta":{"light teal": 4}, "dull crimson": {"light teal": 2}, "posh brown":{"light teal": 3}}')
