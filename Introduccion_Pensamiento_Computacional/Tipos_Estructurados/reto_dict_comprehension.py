print("Dict comprehension")

# Declaracion
# dict_variable = {key:value for (key, value) in dictionary.items()}

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(f"\n dict1= {dict1}")

dict2 = {k: v*2 for (k, v) in dict1.items()}

print(f"\n dict2= {dict2}")


# Usando condicionales

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
print(f"\n numeros: {numeros}")

dict_pares = {k: v for (k, v) in numeros.items() if v % 2 == 0}

print(f" dict_pares: {dict_pares}")
