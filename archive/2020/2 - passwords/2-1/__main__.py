valide = 0
invalide = 0
with open("2.txt", "r") as f:
   psw = f.readlines()

lista_password = [i.split("\n")[0] for i in psw]
for test in lista_password:
    riga = test.split(": ") #divide "9-11 q: xvnlfvhxqfql" in "9-11 q" e "xvnlfvhxqfql"
    condizione = riga[0].split(" ") #divide "9-11 q" in "9-11" e "q"
    minmax = (condizione[0].split("-"))  #divide "9-11" in "9" e "11"

    min = int(minmax[0]) #setto variabile
    max = int(minmax[1]) #setto variabile
    lettera = condizione[1] #setto variabile
    password = riga[1]

#    print(f'Il minimo è {min}, il massimo è {max}, la lettera è {lettera}, la password è: {password}')

    #adesso contiamo quante volte c'è lettera in password
    conta = 0 #numero di caratteri matchati
    for c in password: #per ogni carattere nella password
        if c == str(lettera): #se il carattere è uguale a quello che cerchiamo noi
            conta = conta + 1 #aumentiamo il numero di caratteri
#    print(f'Ci sono {conta} {lettera} in {password}, devono essercene {min}-{max}')
    if conta < min or conta > max: #se il numero è minore del minimo, oppure maggiore del massimo
        invalide = invalide +1
#        print(f'Password INVALIDA!') #ciaone
    else:
#        print(f'Password VALIDA!') #daje
        valide = valide +1

print(f'Password valide: {valide}')
print(f'Password invalide: {invalide}')
