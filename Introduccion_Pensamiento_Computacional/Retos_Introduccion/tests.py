
nombre = input("Ingrese su nombre: ")

print(f'Su nombre es "{nombre}" y tiene {len(nombre)} caracteres')

for caracter in nombre:
    print(caracter)

my_diccionario = {"uno": 1, "dos": 2, "tres": 3}

print(type(my_diccionario))

for val in my_diccionario.keys():
    print(val)

for val in my_diccionario.values():
    print(val)

for val in my_diccionario.items():
    print(f'key= {val[0]}, value= {val[1]}')


