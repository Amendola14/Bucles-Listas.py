'''1. Mostrar los números pares entre dos números que ingresan por teclado.'''

numero_inicial = int(input("Ingrese el número inicial: "))
numero_final = int(input("Ingrese el número final: "))

for i in range(numero_inicial, numero_final+1):
    if i % 2 == 0:
        print(i)