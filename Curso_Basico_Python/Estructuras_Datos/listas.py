
# Lists


def run():

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Hello', True]

    print(my_list)

    print("\nAgrega elemento al final de lista: ")
    my_list.append('Juan')
    print(my_list)

    print("\nInvierte el orden de la lista: ")
    my_list.reverse()
    print(my_list)

    print("\nElimina elemento con el indice que se pasa por parametro: ")
    my_list.pop(0)
    print(my_list)

    print("\nAcompaniar los elementos de lista con indices 0 -(n-1): ")
    for index, value in enumerate(my_list):
        print(index, value)

    print("\nPara iterar sobre dos listas al mismo tiempo: ")
    my_list2 = [10, 11, 12, 13, 14, 15]

    for value_1, value_2 in zip(my_list, my_list2):
        print(value_1, value_2)

    print("\nUnir dos listas en una sola: ")
    print(my_list + my_list2)

    print("\nRepetir la lista n veces en una sola lista: ")
    print(my_list * 5)


if __name__ == '__main__':
    run()
