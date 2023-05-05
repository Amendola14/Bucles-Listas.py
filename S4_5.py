'''5. Hacer programas que generen las siguientes figuras, con la cantidad de niveles ingresados desde teclado '''


'''                           ej 5    a:           '''

n = int(input("ingrese altura:  "))


for i in range (n):
    print("*" * 10)




'''                            ej 5 b:                  '''

n = int(input("ingrese altura:  "))


for i in range (n):
    print("*" * (1+ i) )





'''                             ej 5 c:         '''



n = int(input("ingrese altura:  "))


for i in range (n):

    print("  "  * (n-i) + "*" * (i+1))

'''                             ej 5 d:                         '''



n = int(input("Ingrese la altura de la pirámide: "))
while (n < 1):
    n = int(input("La altura debe ser mayor o igual a 1. Ingrese la altura de la pirámide: "))

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))

'''                     ej 5 e:               '''



niveles= int(input("ingresar niveles: "))
print("-" * 18)

for i in range (niveles):
    print( "|" + " " * 5 + "nivel " +str(niveles-i), " " * 5 + "|" )
    print( "-" * 18)

print( "|" + " " * 8 + "PB" + " " * 8 + "|" )
print( "-" * 18 ) 

'''                                 eje 5 F:                 '''



niveles= int(input("ingresar niveles: "))

print("niveles: ")

for i in range (niveles):
    print(niveles - i, " " * (niveles-i) + "/" + "__" * i + "\\")