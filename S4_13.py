'''''13. Dados como datos 15 números enteros que ingresan por teclado,
determine cuántos de ellos son pares y cuántos impares. Asegurar que ningún
número que se ingresa sea mayor a 99 ni menor a 0'''


# Inicializar contadores

pares=0
impares=0

# Pedir al usuario los 15 números enteros


for i in range (15):
    numero=int(input(f"ingrese un numeros {i+1}: "))

    

# Verificar si el número es válido

if numero  < 0 or numero > 99:
    print("Número inválido. Debe estar entre 0 y 99.")

    # Verificar si el número es par o impar


if numero % 2 == 0:
        pares += 1
else:
        impares += 1

# Mostrar resultados
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")