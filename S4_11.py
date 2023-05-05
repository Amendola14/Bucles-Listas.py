# Pedir un número al usuario
num = int(input("Ingrese un número: "))

# Inicializar variable para determinar si el número es divisible por 3
es_divisible_por_3 = ""

# Imprimir encabezado de la lista
print("N  N x 2  N / 2  Divisible por 3")

# Recorrer números desde el número ingresado hasta 1 (ambos inclusive)
for i in range(num, 0, -1):
    # Calcular valores para cada fila de la lista
    n = i
    n_x_2 = n * 2
    n_div_2 = n / 2
    if n % 3 == 0:
        es_divisible_por_3 = "S"
    else:
        es_divisible_por_3 = "N"
    
    # Imprimir fila de la lista
    print(f"{n}  {n_x_2}  {n_div_2}  {es_divisible_por_3}")
