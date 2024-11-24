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

with open("8.txt") as f:
    file = f.readlines()   
    lines = [line.strip() for line in file] #una lista di tutte le righe così come sono

##part 1

# pos = 0
# tot = 0
# ans = 0

# def exec(pos):
#     global tot
#     comando=lines[pos][:3] #acc
#     arg=lines[pos][3:].strip() #+22
#     # print(f'pos: {pos}\t: {comando} {arg}\t: tot: {tot}')
#     if comando == "acc":
#         lines[pos] = "dne" + " " + arg
#         newpos = pos + 1
#         # print(f'Nuova pos: {pos}')
#         tot += int(arg)
#         # print(f'Nuovo tot: {tot}')
#         print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| ACC! Aumenta il tot di {arg} e vai alla riga successiva {newpos}')
#         exec(newpos)
#     elif comando == "jmp":
#         lines[pos] = "dne" + " " + arg
#         newpos = pos + int(arg)
#         print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| JMP! Fai un salto di {arg} e vai alla riga {newpos}')
#         exec(newpos)
#     elif comando == "dne":
#         print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| DNE! Abbiamo già eseguito questa istruzione')
#         print(f'[Il totale è {tot}]')
#         return 
#     else: #nop
#         lines[pos] = "dne" + " " + arg
#         newpos = pos + 1
#         print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| NOP! Non fare niente e vai alla riga successiva {newpos}')
#         exec(newpos)
# exec(0)


#part2

pos = 0
tot = 0
ans = 0
oldpos= 0
oldcomando = ""
# per ogni linea, copia la lista, swap ed esegui da capo. se arriva alla fine returna il totale, altrimenti resetta la lista e prova con la linea successiva.

def testa():
    trylines = lines.copy()
    end_reached = False
    global tot

    for n in range(len(trylines)):
        print(f'Tentativo numero {n+1}')
        swap(n)
        exec(0)
        if end_reached == True:
            print('Fine del file! Totale {tot}')
            return

#swap cambia un jmp in nop o viceversa
def swap(n):
    global tot
    global trylines
    trylines = lines.copy()
    instr=trylines[n][:4].strip() #acc
    num=trylines[n][4:].strip() #+22
    if instr == "jmp":
        trylines[n] = "nop" + " " + num
        # print(f'Trasformo pos: {oldpos} da "{oldcomando} {oldarg}" a "nop {oldarg}"')
        # input("Press Enter to continue...")
    elif instr == "nop":
        trylines[n] = "jmp" + " " + num
        # print(f'Trasformo pos: {oldpos} da "{oldcomando} {oldarg}" a "jmp {oldarg}"')
        # input("Press Enter to continue...")
    elif instr == "acc":
        return
    print(f"Cambio l'istruzione alla riga {n}: {instr} {num}")
        # input("Press Enter to continue...")

#exec esegue il comando jmp, nop o acc e si accorge quando c'è un loop (se ritorni a un comando già eseguito)
def exec(pos):

    global trylines
    global tot
    global end_reached
    comando=trylines[pos][:3] #acc
    arg=trylines[pos][3:].strip() #+22
    # print(f'pos: {pos}\t: {comando} {arg}\t: tot: {tot}')
    end = len(lines)-1 #600
    if int(pos) == end:
        end_reached = True
        print(f"Success! {tot}")
        exit()        
    if comando == "acc":
        trylines[pos] = "dne" + " " + arg
        newpos = pos + 1
        # print(f'Nuova pos: {pos}')
        tot += int(arg)
        # print(f'Nuovo tot: {tot}')
        # print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| ACC! Aumenta il tot di {arg} e vai alla riga successiva {newpos}')
        exec(newpos)
    elif comando == "jmp":
        trylines[pos] = "dne" + " " + arg
        newpos = pos + int(arg)
        # print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| JMP! Fai un salto di {arg} e vai alla riga {newpos}')
        exec(newpos)
    elif comando == "dne":
        # print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| DNE! Abbiamo già eseguito questa istruzione')
        # print(f'[Il totale è {tot}]')
        print("Fallito!")
        tot = 0
        return 
    else: #nop
        trylines[pos] = "dne" + " " + arg
        newpos = pos + 1
        # print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| NOP! Non fare niente e vai alla riga successiva {newpos}')
        exec(newpos)

testa()








# def exec(pos):
#     global tot
#     global oldpos
#     global oldcomando 
#     global oldarg
#     end = len(lines)-1 #600
#     if int(pos) == end:
#         return True
#     comando=lines[pos][:4].strip() #acc
#     arg=lines[pos][4:].strip() #+22
#     # print(f'pos: {pos}\t: "{comando}" "{arg}"\t: tot: {tot}')

#     if comando == "acc":
#         oldcomando = comando
#         oldarg = arg
#         lines[pos] = "." + comando + " " + arg
#         newpos = pos + 1
#         tot += int(arg)
#         print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| ACC! Aumenta il tot di {arg} e vai alla riga successiva {newpos}')
#         oldpos = pos
#         exec(newpos)
#     elif comando == "jmp":
#         oldcomando = comando
#         oldarg = arg
#         lines[pos] = "." + comando + " " + arg
#         newpos = pos + int(arg)
#         print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| JMP! Fai un salto di {arg} e vai alla riga {newpos}')
#         oldpos = pos
#         exec(newpos)
#     elif comando == "nop": #nop
#         oldcomando = comando
#         oldarg = arg
#         lines[pos] = "." + comando + " " + arg
#         newpos = pos + 1
#         print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| NOP! Non fare niente e vai alla riga successiva {newpos}')
#         oldpos = pos
#         exec(newpos)
#     elif comando[0] == ".": 
#         newcomando=lines[pos][:5].strip(". ") #acc
#         newarg=lines[pos][4:].strip() #+22
#         print(f'pos : {pos} \t: {comando} {arg}\t: tot: {tot}\t| ERR! Abbiamo già eseguito questa istruzione. Ritorniamo a {oldpos}? Era un {oldcomando} {oldarg} - io ero {newcomando} {newarg}')
#         # input("Press Enter to continue...")
#         if oldcomando == "jmp":
#             lines[oldpos] = "nop" + " " + oldarg
#             print(f'Trasformo pos: {oldpos} da "{oldcomando} {oldarg}" a "nop {oldarg}"')
#             # input("Press Enter to continue...")
#         elif oldcomando == "nop":
#             lines[oldpos] = "jmp" + " " + oldarg
#             print(f'Trasformo pos: {oldpos} da "{oldcomando} {oldarg}" a "jmp {oldarg}"')
#             # input("Press Enter to continue...")
#         elif oldcomando == "acc":
#             print(f'pos: {oldpos} è "{oldcomando} {oldarg}" - non trasformo niente')
#             # input("Press Enter to continue...")
#         lines[pos] = newcomando + " " + newarg
#         newpos = oldpos
#         print(f'Ritorno a pos: {newpos}')
#         exec(newpos)
    
exec(0)