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
FILENAME = "inputs/02.txt"
# FILENAME = "inputs/02-test.txt"


lines: list = [l.strip() for l in open(FILENAME).readlines()]

# Part 1
sol1 = 0
pos = (sum(int(x.split()[1]) for x in lines if x.split()[0] == "forward"), sum(int(x.split()[1]) for x in lines if x.split()[0] == "down") - sum(int(x.split()[1]) for x in lines if x.split()[0] == "up"))
print(pos)
sol1 = pos[0] * pos[1]

print(f"Parte 1: [{sol1}]")

   

# Part 2
sol2 = 0
pos = [0, 0]
aim = 0
for instr in lines:
    instr = instr.split()
    if instr[0] == "forward":
        pos[0] += int(instr[1])
        pos[1] += int(instr[1]) * aim
    if instr[0] == "down":
        aim += int(instr[1])
    if instr[0] == "up":
        aim -= int(instr[1])
print(pos)
sol2 = pos[0] * pos[1]


print(f"Parte 2: [{sol2}]")
