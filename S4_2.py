''''2. Imprimir la tabla de multiplicar de un número entero K (que se ingresa por
teclado), entre 1 y 10.'''


k = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{k} x {i} = {k*i}")