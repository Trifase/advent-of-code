import os
import json, numbers

with open("1.txt", "r") as fp:
    num = fp.readlines()

num = [int(i.split("\n")[0]) for i in num]

print("Parte 1\n")
for i in num:   
    if 2020-i in num:
        print(i, 2020-i, i*(2020-i))
        
