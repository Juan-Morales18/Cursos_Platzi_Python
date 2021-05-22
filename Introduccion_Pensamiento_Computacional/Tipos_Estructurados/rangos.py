
print("\nRangos\n")

# Declaracion de rango: range (inicio,fin,pasos)
mi_rango = range(1, 5)

print(type(mi_rango))


for i in mi_rango:
    print(i)

mi_rango = range(0, 7, 2)  # El ultim numero generado es el 6

mi_otro_rango = range(0, 8, 2)  # El ultimo numero generado es el 6

print("\n Comparacion de valores del rango")
if mi_rango == mi_otro_rango:  # Comparacion de valores del rango
    print(True)

print("\nValores generados por 'mi_rango'")
for i in mi_rango:
    print(i)

print("\nValores generados por 'mi_otro_rango'")
for i in mi_otro_rango:
    print(i)

print("\n Comparacion de direcciones de memoria de rangos")
print(mi_rango is mi_otro_rango)
