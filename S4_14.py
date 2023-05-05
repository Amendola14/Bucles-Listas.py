'''' 14. Realizar un programa que permita ingresar pesos de cajas. Finaliza el
ingreso de valores con 0. Las cajas tienen dos categorías según el peso: "A"
entre 50g y 99g y "B" entre 100g y 200g. Al finalizar el ingreso de datos,
informar la cantidad y el promedio del peso de las cajas "A" y la cantidad y
el promedio del peso de las "B". Además mostrar el porcentaje que representa
cada una respecto del total.'''


# contadores
pares = 0
impares = 0

# variables
peso_a = 0
peso_b = 0
cantidad_a = 0
cantidad_b = 0

# ingreso de datos
peso = float(input("Ingrese el peso de una caja (ingrese 0 para finalizar): "))
while peso != 0:
    if peso >= 50 and peso <= 99:
        peso_a += peso
        cantidad_a += 1
    elif peso >= 100 and peso <= 200:
        peso_b += peso
        cantidad_b += 1
    else:
        print("Peso fuera de rango. Debe estar entre 50g y 200g")
    
    peso = float(input("Ingrese el peso de una caja (ingrese 0 para finalizar): "))

#  promedios y porcentajes
if cantidad_a > 0:
    promedio_a = peso_a / cantidad_a
    porcentaje_a = cantidad_a / (cantidad_a + cantidad_b) * 100
else:
    promedio_a = 0
    porcentaje_a = 0

if cantidad_b > 0:
    promedio_b = peso_b / cantidad_b
    porcentaje_b = cantidad_b / (cantidad_a + cantidad_b) * 100
else:
    promedio_b = 0
    porcentaje_b = 0

#  resultados
print("Cajas A:")
print("Cantidad:", cantidad_a)
print("Promedio de peso:", promedio_a, "g")
print("Porcentaje:", porcentaje_a, "%")
print()

print("Cajas B:")
print("Cantidad:", cantidad_b)
print("Promedio de peso:", promedio_b, "g")
print("Porcentaje:", porcentaje_b, "%")
