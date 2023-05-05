
'''Ingresar valores de temperatura (entre 10°C y 50°C) Al finalizar el ingreso
de datos mostrar: mayor, menor, promedio y cantidad de valores ingresados
(finaliza ingresando -1. Evitar ingreso de valores incorrectos.)'''

# Inicializar variables (el float representa numeros reales positivos,negativos y decimales.)
mayor = float('-inf')
menor = float('inf')
suma_temperaturas = 0
cantidad_valores = 0

# Pedir valores de temperatura hasta que se ingrese -1
while True:
    valor_str = input("Ingrese un valor de temperatura (-1 para terminar): ")
    if valor_str == '-1':
        break
    try:
        valor = float(valor_str)
        if valor < 10 or valor > 50:
            print("Valor fuera de rango. Debe estar entre 10°C y 50°C")
            continue
    except ValueError:
        print("Valor ingresado inválido. Intente de nuevo.")
        continue

    # Actualizar valores
    mayor = max(mayor, valor)
    menor = min(menor, valor)
    suma_temperaturas += valor
    cantidad_valores += 1

# Calcular el promedio (si se ingresó al menos un valor)
if cantidad_valores > 0:
    promedio = suma_temperaturas / cantidad_valores
    print(f"Mayor: {mayor}")
    print(f"Menor: {menor}")
    print(f"Cantidad de valores: {cantidad_valores}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron valores de temperatura válidos.")
