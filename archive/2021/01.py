import re

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
FILENAME = "inputs/01.txt"
# FILENAME = "inputs/01-test.txt"


lines: list = [int(l.strip()) for l in open(FILENAME).readlines()]

# Part 1
p1_counter = 0
for n in range(1, len(lines)):
    if lines[n] > lines[n-1]:
        p1_counter += 1
print(f"Parte 1: [{p1_counter}]")

# Part 2
p2_counter = 0
for n in range(1, len(lines) - 2):
    now = sum(lines[x] for x in range(n, n + 3))
    previous = sum(lines[x] for x in range(n - 1, n + 2))
    if now > previous:
        p2_counter += 1
print(f"Parte 2: [{p2_counter}]")
