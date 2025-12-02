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

with open("10.txt") as f:
    file = f.readlines()   
    lines = [int(line.strip()) for line in file] #una lista di tutte le righe così come sono

adaptlist = sorted(lines)
print(f'Lista adattatori = {adaptlist}\n')
oldadapt = 0
steps1 = 0
steps2 = 0
steps3 = 1 #il 3-step finale
i = 0
# print(f'{Fore.WHITE}VOLT\t ADATTATORE\t{Fore.RED}1-jolt\t{Fore.GREEN}2-jolt\t{Fore.BLUE}3-jolt')
# print(f'{Fore.WHITE}----------------------------------------------')
while i < len(adaptlist):
    if adaptlist[i] - oldadapt == 1:
        steps1 += 1
    elif adaptlist[i] - oldadapt == 2:
        steps2 += 1
    elif adaptlist[i] - oldadapt == 3:
        steps3 += 1
    print(f'{Fore.WHITE}v = {oldadapt}\t adap = {adaptlist[i]}\t{Fore.RED}  {steps1}\t{Fore.GREEN}  {steps2}\t{Fore.BLUE}  {steps3}')
    oldadapt =adaptlist[i]
    i += 1
# print(f'{Fore.WHITE}----------------------------------------------')
print(f'{Fore.YELLOW}Soluzione Parte 1: [{steps1*steps3}]')