import random


def generar_contrasenia():
    MAYUS = ('A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    MINUS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    NUMS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    CHARS = ('*', '+', '-', '/', '@', '_', '?', '!',
             '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')

    caracteres = MAYUS + MINUS + NUMS + CHARS  # Une las tuplas en una sola
    contrasenia = []

    for i in range(15):
        caracter = random.choice(caracteres)
        contrasenia.append(caracter)
    # Une los elementos de la lista en un str. No deja separacion entre caracteres
    contrasenia = "".join(contrasenia)

    return contrasenia


def run():
    print("\nPrograma generador de contrasenias seguras")

    contrasenia = generar_contrasenia()
    print(f"\nTu nueva contrasenia es: {contrasenia}")


if __name__ == '__main__':
    run()
