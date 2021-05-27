# Tuples

def run():
    my_tuple = (1, 1, 2, 2, 3, 4, 5)

    print(my_tuple)

    for num in my_tuple:
        print(num)

    print("Asignacion de elementos de tupla a variables")
    tupla_2 = (1, 2, 3)
    x, y, z = tupla_2

    print(f"tupla = {tupla_2} --> x = {x}, y = {y}, z = {z}")

    print(f"Metodo count(): {my_tuple.count(1)}")

    print(f"Metodo index(): {my_tuple.index(1)}")

    print(f"Metodo index con segundo parametro: {my_tuple.index(2,3)}")

    print("Anidacin de tupla: ")
    tupla3 = (1, 2, ('a', 'b'), 3)
    print(f"tupla3 = {tupla3} --->  tupla3[2][1] = {tupla3[2][1]}")


if __name__ == '__main__':
    run()
