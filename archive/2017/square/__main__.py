text = "TEST"
def expand(s):
    result = ''
    for ch in s:
        result = result + ch + ' '
    return result[:-1]

# text = " ".join(context.args) #SQUARE (6) "S Q U A R E" (6*2)-1 = 11
inversetext = text[::-1] #ERAUQS
lung = (len(text)*2)-1
fill = (lung-2)*' '
message = []
message.append(expand(text))
for i in range(1,len(text)-1):
    message.append(text[i]+fill+inversetext[i])
message.append(expand(inversetext))
squared = "\n".join(message)
print(squared)




#S Q U A R E
#Q         R
#U         A
#A         U
#R         Q
#E R A U Q S

