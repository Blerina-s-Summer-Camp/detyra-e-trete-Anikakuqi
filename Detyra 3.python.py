#Lista ne Variabla 
V1 = [22,17,25,-144,0,171]
V2 = [-3,77,2,4,6,8]
varg = V1 + V2
print ("Lista e numrave:", varg)


#Shembull i deklarimit te numrave qift, tek, negativ apo zero ne loop 
for numrat in varg:
    if numrat % 2 == 0:
      print("Nr:",numrat," është Qift")
      
    if numrat % 2 != 0:
        print("Nr:",numrat," është Tek")

    if numrat == 0:
        print("Nr:",numrat," është ZERO / qift")
    
    if ((numrat <= 0) or (numrat == 0)):
        print("Nr:",numrat," është NEGATIV")

nr_qift = [num for num in varg if num % 2 == 0] 
nr_tek = [num for num in varg if num % 2 != 0]
nr_negativ = [num for num in varg if num <= 0]
print("Numrat qift ne varg: ", nr_qift)
print("Numrat tek ne varg: ", nr_tek)
print("Numrat negativ ose Zero ne varg", nr_negativ)

