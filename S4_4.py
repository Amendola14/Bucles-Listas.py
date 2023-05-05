''''Hacer un programa que genere un número de N cifras (se ingresa por teclado) y
pregunte al usuario números hasta que lo adivine.
Mostrar la cantidad de intentos usados para adivinar el número.'''


import random

# Pedir número de cifras del número a adivinar
while True:
    try:
        n_cifras = int(input("Ingrese el número de cifras del número a adivinar: "))
        if n_cifras >= 1:
            break
        else:
            print("El número de cifras debe ser mayor o igual que 1. Intente de nuevo.")
    except ValueError:
        print("Valor ingresado inválido. Intente de nuevo.")

# Generar número aleatorio de n_cifras
num_min = 10 ** (n_cifras - 1)
num_max = (10 ** n_cifras) - 1
num_adivinar = random.randint(num_min, num_max)

# Pedir al usuario que adivine el número en 3 intentos
for i in range(3):
    try:
        num_ingresado = int(input("Ingrese un número para adivinar el número generado: "))
        if num_ingresado == num_adivinar:
            print(f"¡Felicitaciones! Adivinaste el número {num_adivinar} en el intento {i+1}.")
            break
        else:
            print("No es el número correcto. Intente de nuevo.")
    except ValueError:
        print("Valor ingresado inválido. Intente de nuevo.")
else:
    print(f"Lo siento, no adivinaste el número {num_adivinar} en 3 intentos.")
