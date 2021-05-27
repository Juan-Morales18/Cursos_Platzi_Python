# Dictionaries

def run():

    d1 = {'uno': 1, 'dos': 2}
    print(d1.get('uno'))  # 1
    print(d1.get('tres', 'Llave inexistente'))  # Llave inexistente

    lista = d1.items()
    print(lista)
    lista = list(lista)
    print(type(lista[0][1]))

    print(list(d1.keys())[1])
    print(list(d1.values()))

    d1 = {'uno': 1, 'dos': 2}
    d2 = {'dos': 3, 'cinco': 6}
    d1.update(d2)
    print(d1)  # {'uno' : 1, 'dos': 3 , 'cinco': 6}


if __name__ == '__main__':
    run()
