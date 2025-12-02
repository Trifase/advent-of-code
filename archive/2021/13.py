import re
# from rich import print
import copy
from typing import final
from aoc import get_input
import statistics, math, random
import logging
import time
from PIL import Image, ImageDraw 
from collections import Counter

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

def lista(lista):
    for i in lista:
        print(i)

def list_to_string(lista):
    string = ''.join(str(x) for x in lista)
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

def list_replace(lst, old="1", new="10"):
    """replace list elements (inplace)"""
    i = -1
    try:
        while 1:
            i = lst.index(old, i + 1)
            lst[i] = new
    except ValueError:
        pass

def get_key_from_value(my_dict, to_find):
    for k,v in my_dict.items():
        if sorted(v) == sorted(to_find): return k
    return None

DAY = 13
TEST = 0

if TEST:
    FILENAME = f"inputs/{DAY:02d}-test.txt"
else:
    FILENAME = f"inputs/{DAY:02d}.txt"

level = logging.INFO
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)
start_time = time.perf_counter()




# Parsing
input = [l.strip() for l in open(FILENAME).readlines()]
coords = []
instruzioni = []
for line in input:
    if line:
        if line.startswith("fold"):
            line = line[11:]
            x, y = line.split("=")
            instruzioni.append((x, int(y)))
        else:
            x, y = line.split(",")
            coords.append((int(x), int(y)))

# print(coords)
# print(instruzioni)



# Part 1
sol1 = 0



max_x = max([x[0] for x in coords])
max_y = max([x[1] for x in coords])
img_size = (max_x+1, max_y+1)
img = Image.new("RGB", (max_x + 1, max_y + 1), (255, 255, 255))

for pixel in coords:
    img.putpixel(pixel, (0, 0, 0))

# img.show()
tagli = [0, 0]

def fold(axis, pos, img_size, img):
    coords = []

    for x in range(img_size[0]):
        for y in range(img_size[1]):
            pix = img.getpixel((x, y))
            if pix != (255, 255, 255):
                coords.append((x, y))

    if axis == "y": # orizzontale
        tagli[1] += 1
        pixel_affected = [pixel for pixel in coords if pixel[1] > pos]
        for pixel in pixel_affected:
            # img.putpixel(pixel, (0, 125, 0))
            img.putpixel(pixel, (0, 0, 0))
            x = pixel[0]
            y = pos - (pixel[1] - pos)
            # img.putpixel((x, y), (0, 250, 0))
            img.putpixel((x, y), (0, 0, 0))
            
        
    else:
        tagli[0] += 1
        pixel_affected = [pixel for pixel in coords if pixel[0] > pos]
        for pixel in pixel_affected:
            # img.putpixel(pixel, (0, 0, 125))
            img.putpixel((x, y), (0, 0, 0))
            x = pos - (pixel[0] - pos) 
            y = pixel[1]
            # img.putpixel((x, y), (0, 0, 250))
            img.putpixel((x, y), (0, 0, 0))




img2 = copy.deepcopy(img)

# For part 1
for instr in instruzioni[:1]:
    fold(instr[0], instr[1], img_size, img)

newsize = [img_size[0], img_size[1]]
for x in range(tagli[0]):
    newsize[0] = newsize[0] // 2
for y in range(tagli[1]):
    newsize[1] = newsize[1] // 2

# print(newsize)
final_pixels = []

for x in range(newsize[0]):
    for y in range(newsize[1]):
        pix = img.getpixel((x, y))
        if pix != (255, 255, 255):
            final_pixels.append((x, y))

sol1 = len(final_pixels)
print(f"Parte 1: \t[{sol1}]\n=======\n")


# Part 2
# For part 2
tagli = [0, 0]
for instr in instruzioni:
    fold(instr[0], instr[1], img_size, img2)

newsize = [img_size[0], img_size[1]]
for x in range(tagli[0]):
    newsize[0] = newsize[0] // 2
for y in range(tagli[1]):
    newsize[1] = newsize[1] // 2

area_scritta = (0, 0, newsize[0], newsize[1])
img_scritta = img2.crop(area_scritta)
# img_scritta.show()
img_scritta.save("13_part2.png", "PNG")
# print(newsize)

sol2 = 0
sol2 = ""
import climage
output = climage.convert('13_part2.png')



print(f"Parte 1: \t[{sol1}]\n")
# print(f"Parte 2: \t[{sol2}]")
print("Parte 2:")
print(output)
print(f"\nFinito in: {time.perf_counter()- start_time}")
