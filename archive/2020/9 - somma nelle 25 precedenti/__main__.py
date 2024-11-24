import itertools
import math
import os
import re
import sys
from collections import defaultdict
from functools import partial
from typing import Dict, List, Tuple
import pprint
from colorama import init, Fore

init()

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

with open("9.txt") as f:
    file = f.readlines()   
    lines = [int(line.strip()) for line in file] #una lista di tutte le righe così come sono

#lines = list(range(1,30))

def is_valid(n: int, preamble: list):
    # print(f'Provo\tn = {n}, preamble = {preamble} len = {len(preamble)}')
    for i in preamble:
        if int(n)-int(i) in preamble:
            # print (f'Valido! {i} + {n-i} = {n}')
            return True
    return False

sol = 0
for p in range(len(lines)): #per ogni posizione della lista
    p = int(p)
    templist = []
    sol = 0
    # if p < 6: #i primi 5 ce ne freghiamo
    if p < 26: #i primi 25 ce ne freghiamo
        pass
    else:
        templist = lines[p-25:p-0] #ci creiamo una slice della lista originaria, una lista temporanea dei 25 numeri precedenti
        # templist = lines[p-5:p-0] #ci creiamo una slice della lista originaria, una lista temporanea dei 25 numeri precedenti
        # print(f'for {p}\t{lines[p]}\t{templist}\t{len(templist)}') # qua vediamo riga, numero, lista e lunghezza lista(25)
        # ̀̀print(f'Testo: {lines[p]}')
        if is_valid(lines[p], templist) is False:
            # print(f'riga: {p+1}\t{lines[p]} non è la somma di nessuno dei 25 numeri precedenti\n')
            # print(f'preamble:\t{templist}')
            sol = lines[p]
            break  
print(f'{Fore.RED}Soluzione Parte 1: {sol}')

for i in range(len(lines)): #per ogni numero
    # print(f"Inizio da {lines[i]} - cerco i numeri che sommati danno {sol}")
    sum = 0
    listsum = []
    if lines[i] > sol:
        pass
        # print("Troppo grande!")
    elif lines[i] == sol: 
        pass
        # print("Eh eh")
    else:
        while sum < sol:
            # print(f"Siccome {sum} < {sol}")
            if lines[i] == sum:
                i += 1
            listsum.append(lines[i]) #aggiungiamo il numero alla lista lissum
            # print(f'Aggiungo {lines[i]}')
            # print(f'I numeri da sommare sono {listsum}')
            sum = 0
            for n in range(len(listsum)): #sommiamo tutti i numeri nella lista
                sum += listsum[n] 
            i += 1
            # print(f"La somma è: {sum}")
        if sum == sol:  #se la somma è minore di sol
            # print(f'{Fore.RED}Hooray! Ecco la lista {listsum}')
            print(f'{Fore.GREEN}Soluzione Parte 2: {sorted(listsum)[0]+sorted(listsum)[-1]}')
            break
        elif sum > sol:
            pass
            # print(f"Nope! {sum} > {sol}\n")



    # if is_valid(lines[p], templist) is True: #
    #     print("Next!")
    #     pass
    # else:
    #     print("Nope!")


        
