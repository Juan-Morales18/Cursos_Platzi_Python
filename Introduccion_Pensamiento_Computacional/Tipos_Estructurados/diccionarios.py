print("\nDiccionarios")

diccionario = {'Jorge': 20, 'Saul': 23, 'Sandra': 27}
print(diccionario)

print("\n Obtener llaves")
for llave in diccionario.keys():
    print(llave)

print("\n Obtener valores")
for valor in diccionario.values():
    print(valor)

print("\n Obtener valores y llaves")
for valor, llave in diccionario.items():
    print(valor, llave)

print("\nEliminar elemento del diccionario")
del(diccionario['Saul'])
print(diccionario)
