
print ("\nCalculo de raices cuadradas con enumeracion exhaustiva")

numero_objetivo=int(input("\nIngrese el numero para calcular su raiz cuadrada: "))
respuesta=0

while respuesta**2 < numero_objetivo:
    respuesta += 1

if respuesta**2 == numero_objetivo:
    print(f'\n"La raiz cuadrada de {numero_objetivo} es {respuesta}"')
else:
    print(f'\n"{numero_objetivo} no tiene raiz cuadrada exacta"')

