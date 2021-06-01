from array_ import Array


def main():
    mi_array = Array(5)

    print("Relleno de array con valores: ")

    for i in range(len(mi_array)):
        mi_array[i] = i + 1

    print(mi_array)

    print("Recorriendo los elementos del array: ")

    for opcion in mi_array:
        print(opcion)
        # print(mi_array[opcion-1])

    print(f"Tamanio: {mi_array.__len__()}")

    print(f"Elementos en str: {mi_array.__str__()}")

    print(f"Iterador (referencia en memoria): {mi_array.__iter__()}")

    print(f"Obtener un elemento con index 2 : {mi_array.__getitem__(2)}")

    print(f"Actualizar elemento 7 en indice 4 : {mi_array.__setitem__(4,7)}")

    print(f"Elementos en str: {mi_array.__str__()}")


if __name__ == '__main__':
    main()
