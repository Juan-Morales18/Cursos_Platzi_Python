
print("\nCalcula raices cuadradas con el metodo de biseccion")

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

    print(f"respuesta= {respuesta}, error= {respuesta**2 - numero_objetivo}")

print(f"\nLa raiz cuadrada de {numero_objetivo} es {respuesta}")
