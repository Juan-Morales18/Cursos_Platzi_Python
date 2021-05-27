# Videogame Challenge

import random
from random import randint


def run():
    LIMIT = 50
    value = randint(0, LIMIT)
    tries = 6

    number = int(input(f"""
        'ENCUENTRA EL NUMERO QUE LA COMPUTADORA ESTA PENSANDO'
        
        El numero esta entre el 0 y {LIMIT}
        ----Tienes {tries} opotunidades----

        Ingrese su numero: """))

    while number != value:
        tries -= 1

        if tries == 0:
            print("\nSe han acabado tus oportunidades :(, lo sentimos")
            break

        print(f"\n----Te quedan {tries} oportunidades----")

        if number < value:
            print("\nEl numero objetivo es mas grande!")
        else:
            print("\nEl numero objetivo es menor!")

        number = int(
            input("Ingrese otro numero = "))

    if tries > 0:
        print(f"\n\nFelicidades, encontraste el numero {value}")


if __name__ == '__main__':
    run()
