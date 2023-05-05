'''15. Encontrar el número mayor y el número menor de una lista'''

lista = [4, 10, 2, 8, 5, 1]
maximo = float('-inf') #   máximo con  valor  pequeño
minimo = float('inf') #   mínimo con valor  grande

for num in lista:
    if num > maximo:
        maximo = num
    if num < minimo:
        minimo = num

print("El número máximo es:", maximo)
print("El número mínimo es:", minimo)
