import re

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

# Parsing
FILENAME = "inputs/03.txt"
# FILENAME = "inputs/03-test.txt"


lines: list = [l.strip() for l in open(FILENAME).readlines()]

# Part 1
sol1 = 0
gamma = []
epsilon = []
for bit in range(len(lines[0])):
    γ = 1 if sum(int(x[bit]) for x in lines) > len(lines) / 2 else 0
    ε = 0 if γ else 1
    gamma.append(γ)
    epsilon.append(ε)

gamma_rate  = bin_to_dec(list_to_string(gamma),2)
epsilon_rate = bin_to_dec(list_to_string(epsilon),2)
sol1 = gamma_rate * epsilon_rate

print(f"Gamma rate: \t{list_to_string(gamma)} ({gamma_rate})")
print(f"Epsilon rate: \t{list_to_string(epsilon)} ({epsilon_rate})")
print(f"Parte 1: \t[{sol1}]")
print()


# Part 2
sol2 = 0
oxigen_rating = 0
co2_rating = 0

# returns the most common number at index pos. if equal, returns 1
def get_most_common(list: list[str], pos: int):  # return 0 or 1
    mylist = [number[pos] for number in list]
    number_of_1 = mylist.count("1")
    number_of_0 = mylist.count("0")
    if number_of_1 >= number_of_0:
        return 1
    else:
        return 0

# returns the most common number at index pos. if equal, returns 0
def get_least_common(list: list[str], pos: int):  # return 0 or 1
    mylist = [number[pos] for number in list]
    number_of_1 = mylist.count("1")
    number_of_0 = mylist.count("0")
    if number_of_1 >= number_of_0:
        return 0
    else:
        return 1

# returns a reduced list with only numbers with number n at index pos
def get_reduced_list(list: list[str], pos: int, n: int):
    reduced_list = []
    for number in list:
        if number[pos] == str(n):
            reduced_list.append(number)
    return reduced_list

# recursive function that returns the last entry to survive reduction at most common
def get_oxigen_rating(list: list[str], n: int=0):
    if len(list) == 1:
        return list[0]
    else:
        most_common = get_most_common(list, n)
        newlist = get_reduced_list(list, n, most_common)
        return get_oxigen_rating(newlist, n+1)

# recursive function that returns the last entry to survive reduction at least common
def get_co2_rating(list: list[str], n=0):
    if len(list) == 1:
        return list[0]
    else:
        least_common = get_least_common(list, n)
        newlist = get_reduced_list(list, n, least_common)
        return get_co2_rating(newlist, n+1)

oxigen_rating = bin_to_dec(get_oxigen_rating(lines), 2)
co2_rating = bin_to_dec(get_co2_rating(lines), 2)

print(f"Oxigen Rating: \t{get_oxigen_rating(lines)} ({oxigen_rating})")
print(f"CO2 Rating: \t{get_co2_rating(lines)} ({co2_rating})")

sol2 = oxigen_rating * co2_rating
print(f"Parte 2: \t[{sol2}]")


lista_numeri = []
with open('input.txt') as file:
    for line in file.readlines():
        line.strip()
        lista_numeri.append(line)


lista_numeri: list = [l.strip() for l in open('input.txt').readlines()]



counter = 0
for n in range(1, len(lista_numeri)):
    if lista_numeri[n] > lista_numeri[n-1]:
        counter += 1

quanti_sono = counter