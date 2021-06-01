import random


class Array:

    def __init__(self, capacity: int, fill_value=None):
        """
        Args:
            capacity (int): tamanio estatico del array
            fill_value (any, optional): valor de cada posicion, None por  defecto
        """

        self.__capacity = capacity
        self.__items = [fill_value for i in range(self.__capacity)]

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)

    def __iter__(self):
        return iter(self.__items)

    def __getitem__(self, index: int):
        return self.__items[index]

    def __setitem__(self, index: int, new_value):
        self.__items[index] = new_value

    def random_fill(self):

        for i in range(self.__capacity):
            self.__setitem__(i, random.randint(0, 100))

        # for i, v in enumerate(self.items):
        #    self.items[i] = random.randint(0, 100)

    def sequential_fill(self, start: int):
        for i in range(self.__capacity):
            self.__setitem__(i, start)
            start += 1

    def items_summation(self):
        sum = 0
        iterator = self.__iter__()

        for i in range(self.__capacity):
            sum += next(iterator)
        return sum

        # for item in self.__items:
        #    sum += item
        # return sum


def main():
    # Instancia de clase array, inicia con un tamanio de 5
    array = Array(5)

    # Rellena array co numeros aleatorios
    array.random_fill()

    # Muestra el tamanio del array
    print(array.__len__())

    # Consulta los valores del array
    print(array.__str__())

    # Rellena el array con valores secuenciales, se le pasa como argumento un numero de inicio de secuencia
    array.sequential_fill(0)

    # Se consulta nuevamente los valores del array
    print(array.__str__())

    # Muestra la suma de todos los elementos del array
    print(array.items_summation())

    # Reemplaza el valor en un indice que se pasa como argumento
    array.__setitem__(0, 666)

    # Muestra los nuevos valores del array
    print(array.__str__())


if __name__ == '__main__':
    main()
