import re
from rich import print
import copy
import rich
import pprint
import logging
import time
from dataclassy import dataclass

from PIL import Image, ImageDraw 
from collections import Counter, defaultdict
from codetiming import Timer

from utils import SESSIONS, rematch, get_key_from_value, remove_duplicates, dec_to_bin, bin_to_dec, get_data, get_example, split_list, split_in_chunks

YEAR = 2015
DAY = 6

@dataclass
class Light:
    x: int
    y: int
    status: bool = False
    brightness: int = 0

    def toggle(self):
        self.status = not self.status
        self.brightness += 2
    
    def on(self):
        self.status = True
        self.brightness += 1

    def off(self):
        self.status = False
        if self.brightness > 0:
            self.brightness -= 1





#Input parsing
with Timer(name="Parsing", text="Parsing done: \t{milliseconds:.0f} ms"):
    data = get_data(YEAR, DAY, SESSIONS, example=False)
    
    orders = []
    for line in data:
        if line.startswith('toggle'):
            line = line.split()
            x1, y1 = line[1].split(',')
            x2, y2 = line[3].split(',')
            orders.append(['toggle', (int(x1), int(y1)), (int(x2), int(y2))])
        else:
            line = line.split()
            x1, y1 = line[2].split(',')
            x2, y2 = line[4].split(',')
            orders.append([line[1], (int(x1), int(y1)), (int(x2), int(y2))])



matrix = []
for x in range(1000):
    row = []
    for y in range(1000):
        row.append(Light(x, y))
    matrix.append(row)

for order in orders:
    x1, y1 = order[1]
    x2, y2 = order[2]
    action = order[0]

    l = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            match action:
                case 'on':
                    matrix[x][y].on()
                case 'off':
                    matrix[x][y].off()
                case 'toggle':
                    matrix[x][y].toggle()
            l += 1




# Part 1
@Timer(name="Part 1", text="Part 1 done: \t{milliseconds:.0f} ms")
def part1(data):
    sol1 = 0
    for x in range(1000):
        for y in range(1000):
            if data[x][y].status:
                # print(data[x][y])
                sol1 += 1

    return sol1


# Part 2
@Timer(name="Part 2", text="Part 2 done: \t{milliseconds:.0f} ms")
def part2(data):
    sol2 = 0
    for x in range(1000):
        for y in range(1000):
            sol2 += data[x][y].brightness
    return sol2


s1 = part1(matrix)
s2 = part2(matrix)

print("=========================")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")

