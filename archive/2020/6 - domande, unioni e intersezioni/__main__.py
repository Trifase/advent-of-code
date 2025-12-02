
# # from os import linesep


# with open("6.txt") as f:
#     input = f.readlines()   
#     lines = [line.strip() for line in input] #una lista di tutte le righe così come sono

# # print(input)
# #parte 1
# # groups = [] #ogni gruppo è una lista vuota
# # current = set() #il set da infilare dentor il grupo è vuoto
# # for line in lines: #per ogni linea
# #     if line != '': #se è diversa da linea vuota
# #         for c in line: #per ogni carattere della linea
# #             current.add(c) #aggiungi il carattere al set
            
# #     else: #se invece la linea è vuota
# #         groups.append(current) #aggiungi il set alla lista di caratteri
# #         current = set() #resetta il set

# # groups.append(current) #ultimo gruppo che non ha la riga vuota finale

# #print(f'La somma di tutti i gruppi è: {sum(len(g) for g in groups)}') #per ogni g in gruppo, vedi quanto è lungo e poi sommi tutte le lunghezze

# #parte 2
# lines = ['l', 'l', 'vlqb', '', 'a', 'ab', 'abc', '']
# groups = [] #una lista che contiene tutti i gruppi
# group = [] #una lista per il singolo gruppo
# current = set() #un set di caratteri
# for line in lines: #per ogni linea nel documento
#     if line != '': #se la linea non è la linea vuota
#         for c in line: #per ogni carattere della linea
#             current.add(c) #aggiungi il carattere alla lista
#         group.append(current) #aggiungi il set alla lista group
#         current = set() #resetto current, COGLIONE
#     else:
#         groups.append(group) #se invece la linea è vuota, aggiungi la lista group alla lista groups
#         group = [] #resetta la lista group
        

# groups.append(group)

# print(f'lines = {lines}')
# print(f'groups = {groups}')
# sum = 0

# for i in range(len(groups)):
#     listaset =[]
#     for x in groups[i]:
#         listaset.append(x)
#     sum = sum + len(set.intersection(*groups[i]))
# print(sum)



# groups=[[(a,b,c),(d,e,f)],[(g,h,i),(l,m,n)]]
# i = 0
# groups[i] = [(a,b,c),(d,e,f)]
# *groups[i] = (a,b,c),(d,e,f)

#with open("prova.txt") as f:
#	file = f.readlines()
#	lines = [line.strip() for line in file]
# with open("day6.txt") as f:
# 	file = f.readlines()
# 	lines = [line.strip() for line in file]
lines = ['l', 'l', 'vlqb', '', 'a', 'ab', 'abc', '']

answers = set() #un set per contenere tutte le risposte di una persona
persons = [] # una lista per contenere tutte le persone del gruppo e le loro risposte
groups = [] # una lista per contenere tutti i gruppi di persone
same_answers = set() # una lista per contenere tutte le risposte uguali
sum_answers = [] # una lista per contenere le somme delle risposte
for line in lines: # per tutte le linee del file
    if line != "": #se la linea non è una linea vuota
        for char in line: # per ogni carattere della linea
            answers.add(char) #aggiungi la risposta al set delle risposte
        persons.append(answers) # aggiungi il set di risposte (aka la persona) al gruppo di persone
        answers = set() # resetta il set per prepararlo ad accogliere le risposte della prox persona (se usi set.clear() lo cancelli anche da persons)
    else:
        print(f"Persone: {persons}")
        groups.append(persons) # metto la lista di persone nella lista dei gruppi
        print(f"Gruppi: {groups}")
        print(f"Lunghezza gruppi: {len(groups)}")
        for i in range(len(groups)): #per ogni numero da 0 fino al numero totale di elementi in groups
            same_answers = set.intersection(*groups[i]) 
        print(f"Risposte uguali: {same_answers}")	
        sum_answers.append(len(same_answers))
        persons = []
        same_answers = set()
        print(f"Somma delle risposte uguali: {sum_answers}")
print(sum(sum_answers))
        
	

	
