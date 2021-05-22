print("\nListas")

mi_lista = [1, 2, 3, 4, 5]

print("\nAcceso por Indice")
print(mi_lista[1], mi_lista[2])

print("\nPariticion de lista en rebanadas")
print(mi_lista[::2])

print("\nAdicion de elemento al final")
mi_lista.append('4')
print(mi_lista)

print("\nIteracion sobre lista")
for elemento in mi_lista:
    print(elemento)

# Es preferible clonar una lista para actividades posteriores y no copiarla para evitar efectos secundarios

a = [1, 2, 3]
b = a  # (Copia) "b" apunta a la misma direccion de memoria de "a"

print(f"a={a}   b={b}")

# Se modifica el valor de la direccion de memoria a la que apuntan "a" y "b"
b.append(5)
print(f"a={a}  b={b}")

c = [5, 6, 7]
d = c[::]  # Se clona la lista, "d" toma otra direccion en memoria
d.append(9)

print(f"c= {c}   d={d}")

print("\nList comprehension")
lista = list(range(100))
print(f"lista= {lista}")

pares = [i for i in lista if i % 2 == 0]
print(f"\nValores pares de 'lista' : {pares}")

mult = [i*2 for i in lista]
print(f"\nValores de 'lista' multiplicados por 2: {mult}")
