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

FILENAME = "14-test3.txt"

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
    
def applymask(mask,dec):
    m = []
    b = []
    for c in mask:
        m.append(c)
    for c in str(bin(int(dec))[2:]).zfill(len(mask)):
        b.append(c)
    # print(f'mask=\t{m}')
    # print(f'b=\t{b}')
    old_b_string =''.join([str(x) for x in b])
    for c in range(len(m)):
        if m[c] != "X":
            b[c] = m[c]
    b_string = ''.join([str(x) for x in b])
    m_string = ''.join([str(d) for d in m])
    newdec = int(b_string, 2)
    # print(f'new=\t{b}')
    # print()
    # print(f'm=\t{mask}\nb=\t{old_b_string}\t{dec}\nnb=\t{b_string}\t{newdec}')
    return newdec

def solvex(mask,addr,dec): #solvex("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X","000000000000000000000000000000101010",100)
   
    # print(f'Solvo.\n{Fore.RED}mask\t{mask}\n{Fore.GREEN}addr\t{addr}')
    bin_mask = []
    bin_addr = []
    original_mask = mask #000000000000000000000000000000X1001X
    bin_mask = string_to_list(mask) 
    bin_addr = string_to_list(addr) 
    if "X" in bin_mask:
        for c in range(len(bin_mask)): #for 0-35
            if bin_mask[c] == "1":  #SE 1 in mask       
                bin_addr[c] = "1"   #metti 1 in addr    000000000000000000000000000000101010
            if bin_mask[c] == "X":  #se X in mask
                bin_mask[c] = "#"  #metti # in mask
                newmask = list_to_string(bin_mask) # newmask =  000000000000000000000000000000#1001X            
                bin_addr[c] = "0" # metto lo 0 in addr
                newaddr = list_to_string(bin_addr) #new         000000000000000000000000000000001010
                solvex(newmask,newaddr,dec)#     000000000000000000000000000000#1001X,000000000000000000000000000000001010
                bin_addr[c] = "1" # metto lo 1, re_feedo
                newaddr = list_to_string(bin_addr)
                solvex(newmask,newaddr,dec)
        
    else:
        # print("Non ci sono X")
        # print(type(bin_mask))
        # for c in range(len(bin_mask)):
        #     if bin_mask[c] == "1":
        #         print("Trovato 1")
        #         bin_addr[c] = "1"
            
        newaddr = list_to_string(bin_addr)
        addresses.append(newaddr)
        # print(f"Aggiungo: {newaddr}")
        # print()
    
    return addresses


# instruzioni = {mask:{addr:dec, addr2:dec2}, mask2:{addr3:dec3, addr4:dec4}}
# mem = {addr:bin, addr:bin}
mem = {}
addresses = []

# mask = 10X0110X11XX101XX1000011001001010100
# mem[13197] = 7957847
# mask = 1000110011111X11X1XXXX1X000X010011X1
# mem[25308] = 257586




for i in lines:
    if i.startswith("mask"):
        mask = ""
        l = i.split(" = ")
        mask = l[1]
        print()                                                                         #########DEBUG
        print(f'mask = {mask} - #X: {mask.count("X")} - [{2**(mask.count("X"))}] ')     #########DEBUG
    if i.startswith("mem"):
        addr, dec = rematch(r"mem\[([\d]+)\]\W\W\W([\d]+)", i).groups()
        # b = bin(int(dec))[2:]
        # newdec = solvex(mask,dec_to_bin(addr,36),dec)
        addresses = []
        print(f'addr = {addr}\tvalore = {dec}', end="    ")                             #########DEBUG
        addresses = removeduplicates(solvex(mask,dec_to_bin(addr,36),dec))
        print(f'\t[len: {len(addresses)}]\n')                                           #########DEBUG
        # for i in addresses:                                                             #########DEBUG
            # print(f'{i} - {bin_to_dec(i,2)} - {dec}')                                   #########DEBUG
        for i in addresses:
            # print(i)
            mem[bin_to_dec(i,2)] = int(dec)
        templist = [bin_to_dec(i,2) for i in addresses]
        print(templist)
        # print()
        # mem[addr] = newdec
#print()

pp = pprint.PrettyPrinter(indent=3,width=2)

print()                                                                                 #########DEBUG
# pp.pprint(mem)                                                                        #########DEBUG


print(f'{Fore.RED}La soluzione alla parte 2 è: {Fore.GREEN}[{sum(mem.values())}]') #expected: # 5030603328768

