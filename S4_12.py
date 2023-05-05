'''11. Generar una tabla con encabezado, seis filas y las siguientes
columnas: número, par, impar, múltiplo de 3, primo.
El número inicial se ingresa por consola
En la tabla se marca en con X las condiciones que cumple cada número.'''


# Inicializar contadores
menores_igual_200 = 0
entre_200_y_400 = 0
mayores_igual_400 = 0

# Pedir al usuario la cantidad de ventas
cantidad_ventas = int(input("Ingrese la cantidad de ventas: "))

# Inicializar contadores
menores_igual_200 = 0
entre_200_y_400 = 0
mayores_igual_400 = 0

# Pedir al usuario el monto de cada venta y actualizar contadores
for i in range(cantidad_ventas):
    monto_venta = float(input(f"Ingrese el monto de la venta {i+1}: "))
    if monto_venta <= 200:
        menores_igual_200 += 1
    elif monto_venta < 400:
        entre_200_y_400 += 1
    else:
        mayores_igual_400 += 1

# Mostrar resultados
print(f"Ventas de $200 o menos: {menores_igual_200}")
print(f"Ventas mayores a $200 pero menores a $400: {entre_200_y_400}")
print(f"Ventas de $400 o más: {mayores_igual_400}")