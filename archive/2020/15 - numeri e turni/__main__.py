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

FILENAME = "15.txt"
# FILENAME = "15-test.txt"

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
with open(FILENAME) as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una floor di tutte le righe così come sono

numeri_iniziali = list(lines[0].split(","))
# print(numeri_iniziali)
# print(type(numeri_iniziali))

max = 30000000

gioco = {} #{n:[turno, turno, turno]}

t = 1 #turno
lastspoken = "ble"

# ̀̀0,3,6,0,3,3,1,8,4,0

for i in numeri_iniziali:
    # print(f'[{t}]\t', end="")
    listaturni = []
    listaturni.append(t)
    gioco[i] = listaturni
    last_spoken = i
    t += 1
    
    # print(f'{i}')
#
#print(f'Fine round iniziale\nt = {t}, last_spoken = {last_spoken}, gioco = {gioco}')
#print()
# print("----------")
while t-1 < 30000000:
    if t%100000 == 0:
        print(t)
    i = last_spoken
    # print(f'[{t}] [{i}]->\t', end="")
#    print("Non è ancora il turno [2020]")

#    print(f'i = last_spoken [i = {last_spoken}]')
    if i in gioco:
#        print(f"{i} esiste:")
        if len(gioco[i]) > 1:
#            print(f'i [{i}] è stato già detto prima due volte')
            turniprima = str(int(gioco[i][-1]-int(gioco[i][-2])))
#            print(f'Al turno {int(gioco[i][-1])} e al turno {int(gioco[i][-2])} - {turniprima} turni fa')
            last_spoken = turniprima
#            print(f'quindi adesso diciamo: {turniprima} e passiamo al prossimo turno')
            if last_spoken in gioco:
                if len(gioco[last_spoken]) > 1:
                    gioco[last_spoken].pop(-2)
                    gioco[last_spoken].append(t)
#                    print(f'debug: gioco[last_spoken] è {gioco[last_spoken]}')
                else:
                    gioco[last_spoken].append(t)
#                    print(f'debug: gioco[last_spoken] è {gioco[last_spoken]}')
                t += 1
            else:
                gioco[last_spoken] = [t]
                t += 1
#            print(f'Prossimo turno è il turno {t}, l\'ultimo numero detto è {last_spoken}')
#            print(gioco)
#            print()
    
        else:
            
            # len(gioco[i]) == 1: # è stato detto una volta sola, il turno precedente
#            print(f'i [{i}] è stato già detto prima una volta, cioè il turno precedente, insomma quello che stiamo cercando.')
            last_spoken = '0'
#            print(f'imposto last_spoken a 0; last_spoken = {last_spoken}')
            if len(gioco[last_spoken]) > 1:
                gioco[last_spoken].pop(-2)
                gioco[last_spoken].append(t)
#                print(f'debug: gioco[last_spoken] è {gioco[last_spoken]}')
            else:
                gioco[last_spoken].append(t)
#                print(f'debug: gioco[last_spoken] è {gioco[last_spoken]}')
            t += 1
#            print(f'Prossimo turno è il turno {t}, l\'ultimo numero detto è {last_spoken}')
#            print(gioco)
#            print()
    else:
#        print(f"{i} non esiste:")
        listaturni = []
        listaturni.append(t)
        gioco[i] = listaturni
        last_spoken = i
        t += 1
    # print(f'{last_spoken}')
#        print(f'Prossimo turno è il turno {t}, l\'ultimo numero detto è {last_spoken}')
#        print(gioco)
#        print()
# print(gioco)
print(f'{Fore.GREEN}GIOCO CONCLUSO! Ultimo numero pronunciato al turno {t-1}: {last_spoken}')

                

        

    #     else:
    #         last_spoken = '0'

        
        
    #     if i not in gioco:
    #         print(f"if i not in gioco:   [i = {i}]")
    #         last_spoken = '0'
    #         print(f"last_spoken = '0'")
    #         listaturni = [t]
    #         print(f"listaturni = [t]:   [t = {t}]")
    #         gioco[last_spoken] = listaturni
    #         print(f"gioco[last_spoken] = listaturni:   listaturni = {listaturni}")
    #         t += 1
    # except:

        # pass

# PROVA CON
# gioco = {numero: [turni]}
#se last spoken in gioco.keys, prendi lista=gioco[key] e cerca quando è stato il turno, e confrontalo con il t di adesso. aggiungi il (la differenza) a gioco[key][lista]

# while t <= max:
#     print(t,end=" ")
#     # print()
#     # print(f'{Fore.CYAN}Iniziamo. E\' il turno [{t}]. Nel turno di prima [{t-1}] abbiamo detto il numero [{last_spoken}]')
#     # print("Non è ancora il turno {max}")
#     valori = list(gioco.values())
#     valori.pop()
#     if last_spoken not in valori: #mai detto prima
#         # print(f"Il numero {last_spoken} non è mai stato detto prima")
#         gioco[t] = '0'
#         t += 1
#         last_spoken = '0'
#         # print(f"Il nuovo last spoken = [0]. Si va prossimo turno, il turno [{t}]")
#         # print(gioco.values())
#     else:
#         # print(f"ATTENZIONE! Il numero [{last_spoken}] è già stato detto.")
#         valori = list(gioco.values()) #[0,3,6,0]
#         # print(f'Lista numeri precedenti: {valori}, noi cerchiamo [{last_spoken}]')
#         # print(f'Lista al contrario:\t {valori[::-1]}')
#         for i in range(1, len(valori[::-1])):   #[0,6,3,0]
#             if valori[::-1][i] == last_spoken:
#                 # print(f'[{last_spoken}] trovato! Posizione [{i}] (nella lista invertita)')
#                 # print(f"L'abbiamo detto {i} turni fa")
#                 last_spoken = str(i)
#                 # print(f'{Fore.RED}Nel turno {t} diciamo: {i}')
#                 gioco[t] = last_spoken
#                 t += 1
#                 break
#             else:
#                 pass
#                 # print(f"Non l'abbiamo detto {i} turni fa... cerco ancora")
        
#     # print("Si va al prossimo turno...")
#     # print("Ecco la partita fino ad adesso")
#     # print(gioco.values())


# print(f'{Fore.GREEN}GIOCO CONCLUSO! Ultimo numero pronunciato: {last_spoken}')
# # print(list(gioco))  
# # print(list(gioco.values()))  

# # print(f'turno: {t}\t ultimo numero detto: {last_spoken}')

# # print("Intera partita")
# # print(gioco)

# # print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{     }]') #expected: # 436

