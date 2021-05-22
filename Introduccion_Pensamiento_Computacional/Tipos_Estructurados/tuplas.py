
print("Tuplas\n")

mi_tupla = (1, 'dos', 'tres', True, 5.0)

print(mi_tupla[0], mi_tupla[3])  # Obtencion de valores de tupla por indice

print("\nImpresion de valores de tupla")
for val in mi_tupla:
    print(f"valor= {val}")

print("\nDefinicion de tupla de un solo valor")
tupla = (1,)  # Definicion de tupla de un solo valor
print(type(tupla))

print("\nReasignacion de tupla")
otra_tupla = (2, 3, 4, 5)
tupla += otra_tupla  # Reasignacion de Tupla

print("Valores de tupla: ", tupla)

print("\nDesempaquetado de Tupla")
a, b, c, d, e = tupla
print(f"a= {a} , b= {b}, c= {c}, d= {d}, e= {e}")


print("\nRetornos multiples de funcioes con tuplas")


def coordenadas():
    return (3, 2)


x, y = coordenadas()
print(f"x= {x}, y= {y}")
