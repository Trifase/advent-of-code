import os
import json, numbers

with open("1.txt", "r") as file:
    num = file.readlines()

num = [int(i.split("\n")[0]) for i in num]

for a in num:
    for b in num:   
        if 2020-a-b in num:
            print (a, b, 2020-a-b, ": ", a*b*(2020-a-b))