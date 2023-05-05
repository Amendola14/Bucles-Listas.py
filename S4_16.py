import random

secreto = random.randint(1, 10)
intentos = 0

print("Bienvenido al juego de adivinar un número del 1 al 10")
print("Tienes 5 intentos para adivinar el número secreto")

while intentos < 5:
    intento = int(input("Ingresa un número entre 1 y 10: "))
    intentos += 1
    
    if intento == secreto:
        print("Adivinaste en el intento número", intentos)
        break
    elif intento < secreto:
        print("El número secreto es mayor a", intento)
    else:
        print("El número secreto es menor a", intento)
        
    if intentos == 5:
        print("Lo siento, no lograste adivinar el número secreto. Era", secreto)
