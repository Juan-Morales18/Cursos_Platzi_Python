
print("\nCalcula raiz cuadrada con aproximaciones sucesivas")

numero_objetivo = int(
    input('\nIngrese el numero para calcular su raiz cuadrada: '))

epsilon = 0.1  # Margen de error para encontrar la raiz cuadrada

paso = epsilon**2  # Distancia entre valores a probar

respuesta = 0.0

while abs(respuesta**2 - numero_objetivo) >= epsilon and respuesta <= numero_objetivo:

    print(abs(respuesta**2 - numero_objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - numero_objetivo) >= epsilon:
    print(f'\nNo se encontro la raiz cuadrada de {numero_objetivo}')
else:
    print(f'\n"La raiz cuadrada de {numero_objetivo} es {respuesta}"')
