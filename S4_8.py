'''8. Dados como datos 10 números enteros (se ingresan por teclado), obtener la
suma de los números impares y el promedio de los números pares.'''

suma_impares = 0
suma_pares = 0
cantidad_pares = 0

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))

    if num % 2 == 0:
        suma_pares += num
        cantidad_pares += 1
    else:
        suma_impares += num

promedio_pares = 0
if cantidad_pares != 0:
    promedio_pares = suma_pares / cantidad_pares

print(f"La suma de los impares es: {suma_impares}")
print(f"El promedio de los pares es: {promedio_pares}")     