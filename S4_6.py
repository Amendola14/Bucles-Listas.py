'''6. Un corredor de seguros necesita cobrar a su lista de clientes morosos.
Nos pide que calculemos el valor de la deuda, ingresando el total anual de la
póliza y los meses adeudados.'''


poliza=int(input("ingresa el total anual de la póliza: "))
meses=int(input("Por favor, ingresa los meses adeudados: "))

while poliza !=0:
    poliza_mes = poliza / 12
    print("pliza anual: ", poliza)
    print("meses adeudados: ", meses)
    print("deuda total: ", meses * poliza_mes)

    poliza:int(input("ingresa 0 si quuiere terminar o el valor  de poliza para continuar: "))
    meses:int(input(" ingresa 0 si quuiere terminar o el valor  de meses adeudados para continuar: "))