valide = 0
invalide = 0
with open("2.txt", "r") as f:
   psw = f.readlines()

lista_password = [i.split("\n")[0] for i in psw]
for test in lista_password:
#    test1 = "9-11 q: xvnlfvhxqfql" #stringa di testo da controllare
#   test = "3-6 r: rrrvrmr"
    riga = test.split(": ") #divide "9-11 q: xvnlfvhxqfql" in "9-11 q" e "xvnlfvhxqfql"

    condizione = riga[0].split(" ") #divide "9-11 q" in "9-11" e "q"
    minmax = (condizione[0].split("-"))  #divide "9-11" in "9" e "11"

    pos1 = int(minmax[0]) #setto variabile
    pos2 = int(minmax[1]) #setto variabile
    lettera = condizione[1] #setto variabile
    password = riga[1]

    print(f'La prima posizione è {pos1}, la seconda posizione è {pos2}, la lettera è {lettera}, la password è: {password}')

    #compariamo se l'n-esimo carattere è uguale a carattere. aggiustato per colpa degli indici che partono da 0
    #inoltre lo XOR ^ funziona solo bitwise quindi passiamo da bool per avere 1 e 0
    if bool(password[pos1-1] == lettera) ^ bool(password[pos2-1] == lettera): 
        print('Password VALIDA')
        valide = valide +1
    else:
        print ('password INVALIDA')
        invalide = invalide +1

print(f'Password valide: {valide}')
print(f'Password invalide: {invalide}')
