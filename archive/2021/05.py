import re
from rich import print
import copy
from PIL import Image

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

# Parsing

FILENAME = "inputs/05.txt"
# FILENAME = "inputs/05-test.txt"

lines= [l.strip() for l in open(FILENAME).readlines()]

def count_bright_pixels(img: Image, brightness: int) -> int:
    total = 0
    pixvals = list(img.getdata())
    for pixel in pixvals:
        if pixel > brightness:
            total += 1
    return total

def draw_vents(img_size: tuple[int], lines: list[str], brightness: int, diagonali=False):
    def brighten_pixel(img: Image, coord: tuple[int], brightness: int) -> None:
        value = img.getpixel((coord[0], coord[1]))
        img.putpixel((coord[0], coord[1]), value + brightness)
        return
   
    img = Image.new("L", img_size) 
    for vent in lines:
        # print("====")
        # print(vent)

        vent_points = set()
        start_end = vent.split(' -> ')
        origin = tuple(int(x) for x in start_end[0].split(','))
        end = tuple(int(x) for x in start_end[1].split(','))
        
        if origin[0] == end[0]:  # verticale
            x = origin[0]
            y = origin[1]
            if y < end[1]:  # verso giu
                while y <= end[1]:
                    # print(x, y)
                    vent_points.add((x, y))
                    y += 1
                    
            else:  # verso su
                while y >= end[1]:
                    vent_points.add((x, y))
                    y -= 1

        elif origin[1] == end[1]:  # orizzontale
            x = origin[0]
            y = origin[1]
            if x < end[0]:  # verso dx
                while x <= end[0]:
                    # print(x, y)
                    vent_points.add((x, y))
                    x += 1
                    
            else:  # verso sx
                while x >= end[0]:
                    vent_points.add((x, y))
                    x -= 1
        else:  
            if diagonali == False:
                continue# è diagonale
            else:
                # print("E' diagonale.")
                # Siccome sono stanco, farò semplicemente i quattro casi di retta diagonale.
                x = origin[0]
                y = origin[1]
                if (x < end[0]) and (y < end[1]):  # caso 1, entrambi a crescere
                    # print("Caso 1")
                    while x <= end[0]:
                        # print(x, y)
                        vent_points.add((x, y))
                        x += 1
                        y += 1
                elif (x > end[0]) and (y > end[1]):  # caso 2, entrambi a diminuire
                    # print("Caso 2")
                    while x >= end[0]:
                        # print(x, y)
                        vent_points.add((x, y))
                        x -= 1
                        y -= 1
                elif (x > end[0]) and (y < end[1]):  # caso 3, uno diminuisce l'altro aumenta
                    # print("Caso 3")
                    while x >= end[0]:
                        # print(x, y)
                        vent_points.add((x, y))
                        x -= 1
                        y += 1
                else:  # caso 4, il contrario del caso 3
                    # print("Caso 4")
                    while x <= end[0]:
                        # print(x, y)
                        vent_points.add((x, y))
                        x += 1
                        y -= 1



        for point in vent_points:
            brighten_pixel(img, (point[0], point[1]), brightness)
    return img


# Part 1
sol1 = 0
img = draw_vents((1000,1000), lines, brightness=30, diagonali=False)
sol1 = count_bright_pixels(img, 30)
print(f"Parte 1: \t[{sol1}]")


# Part 2
sol2 = 0
img = draw_vents((1000,1000), lines, brightness=30, diagonali=True)
sol2 = count_bright_pixels(img, 30)
print(f"Parte 2: \t[{sol2}]")
img.show()

