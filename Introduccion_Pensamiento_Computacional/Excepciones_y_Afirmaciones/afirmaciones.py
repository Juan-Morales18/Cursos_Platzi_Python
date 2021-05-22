
def suma(a, b):
    """Suma dos numeros enteros

    param a int 
    param b int

    return a+b
    """
    assert(type(a) == int)
    assert(type(b) == int), "Argumentos no enteros"

    return a+b


print(suma(5, 3))
print(suma(5, 5))


def primera_letra(lista_de_palabras):
    """Devuelve lista con primeras letras de lista de palabras

    param lista_de_palabras list

    return list
    """
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras


lista_de_palabras = ['Luis', 'Ulises', 'Ignacio', 'Saul']

print(primera_letra(lista_de_palabras))


print(5/'Platzi')
