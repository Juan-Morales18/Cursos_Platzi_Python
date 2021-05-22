
def enumeracion_exhaustiva():
    numero_objetivo = int(
        input("\nIngrese el numero para calcular su raiz cuadrada: "))
    respuesta = 0

    while respuesta**2 < numero_objetivo:
        respuesta += 1

    if respuesta**2 == numero_objetivo:
        print(f'\n"La raiz cuadrada de {numero_objetivo} es {respuesta}"')
    else:
        print(f'\n"{numero_objetivo} no tiene raiz cuadrada exacta"')


def aproximacion_de_soluciones():
    numero_objetivo = int(
        input('\nIngrese el numero para calcular su raiz cuadrada: '))

    epsilon = 0.1  # Margen de error para encontrar la raiz cuadrada

    paso = epsilon**2  # Distancia entre valores a probar

    respuesta = 0.0

    while abs(respuesta**2 - numero_objetivo) >= epsilon and respuesta <= numero_objetivo:

        respuesta += paso

    if abs(respuesta**2 - numero_objetivo) >= epsilon:
        print(f'\nNo se encontro la raiz cuadrada de {numero_objetivo}')
    else:
        print(f'\n"La raiz cuadrada de {numero_objetivo} es {respuesta}"')


def busqueda_binaria():
    numero_objetivo = int(
        input("\nIngrese un numero para calcular su raiz cuadrada: "))

    # Primer intervalo o espacio de prueba
    bajo = 0.0
    alto = numero_objetivo

    epsilon = 0.00001  # Error permitido

    respuesta = (bajo + alto) / 2  # Punto medio del intervalo

    while abs(respuesta**2 - numero_objetivo) >= epsilon:

        if respuesta**2 < numero_objetivo:
            bajo = respuesta  # Se ajusta intervalo (Se toma mitad superior)
        else:
            alto = respuesta  # Se ajusta intervalo (Se toma mitad inferior)

        respuesta = (bajo + alto)/2  # Punto medio del nuevo intervalo

    print(f"\nLa raiz cuadrada de {numero_objetivo} es {respuesta}")


print("\n Programa para calcular raices cuadradas por diferentes metodos")

print("""Seleccione el metodo de calculo
        1. Enumeracion Exhaustiva
        2. Aproximacion de Soluciones
        3. Busqueda Binaria
        """)

opcion = 0

while opcion < 1 or opcion > 3:
    opcion = int(input("Ingrese numero de opcion: "))

if opcion == 1:
    enumeracion_exhaustiva()
elif opcion == 2:
    aproximacion_de_soluciones()
else:
    busqueda_binaria()
