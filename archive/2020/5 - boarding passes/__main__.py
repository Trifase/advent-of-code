with open("5.txt", "r") as fp:
    lines = fp.readlines()

lines = [line[:-1] for line in lines]
#print(input)
# lista_pass = []


#test = ["BFBBFBBRRL", "BFBFFFFLLL", "BBFFBFBLRR"]
ids = []
def boarding(bpass):
    
    row = 0
    column = 0
    ID = 0

    r = bpass[:7] #i primi sette caratteri
    print(f'Boarding Pass: {bpass}')
    start = 0
    end = 127
    for char in r:
        #print(f'Carattere {char}')
        if char == "F":
            end = int((start+end+1)/2) - 1
        elif char == "B":
            start = int((start+end+1)/2)
        #print(f'Start: {start} - End: {end}')
    row = start
    r = bpass[7:] #ultimi tre caratteri
    start = 0
    end = 7
    for char in r:
        #print(f'Carattere {char}')
        if char == "L":
            end = int((start+end+1)/2) - 1
        elif char == "R":
            start = int((start+end+1)/2)
            #print(f'Start: {start} - End: {end}')
    column = start
    ID = row*8 + column
    print(f'Fila: {row} Colonna: {column} ID: {ID}')
    ids.append(ID)


# test = "BBFFFFRRR"
# boarding(test)

for line in lines:
    boarding(line)  

print(f'ID più alto: {max(ids)}') #soluzione 1
print(f'ID più basso: {min(ids)}')

#soluzione 2
for i in range(min(ids),max(ids)):
    if (i + 1 in ids) and (i - 1 in ids):
        if i not in ids:
            print(f'Un ID mancante: {i}')
        


