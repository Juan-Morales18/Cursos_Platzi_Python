def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


def main():
    print("Programa que calcula el factorial de un numero")

    numero = int(input("Ingrese un numero: "))

    print(f"El factorial de {numero} es = {factorial(numero)}")


if __name__ == '__main__':
    main()
