'''El factorial de un número n (n!) es el producto de todos los números enteros
positivos menores o iguales que n
Ej. el factorial de 5 es: 5 x 4 x 3 x 2 x 1 = 120'''

n = int(input("Ingrese un número para calcular su factorial: "))

factorial = 1

if n == 0:
    factorial = 1
else:
    for i in range(1, n+1):
        factorial *= i

print(f"El factorial de {n} es {factorial}")