'''7. Hacer un programa que multiplique p x q mediante sumas sucesivas. (p y q se
ingresan por consola)'''

# Pedimos al usuario que ingrese los valores de p y q
p = int(input("Ingrese el valor de p: "))
q = int(input("Ingrese el valor de q: "))

# Inicializamos el resultado en cero
resultado = 0

for i in range(q):
    resultado += p

print(f"El resultado de la multiplicación {p} x {q} es: {resultado}")
