# Crete an array

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()

        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_value):
        self.items[index] = new_value


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
