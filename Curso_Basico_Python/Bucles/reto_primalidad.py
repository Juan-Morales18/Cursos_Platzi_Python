def run():
    number = int(input("Ingrese un numero para averigiar si es primo: "))

    if is_primo(number):
        print(f" {number} es primo")
    else:
        print(f"{number} no es primo")


def is_primo(number):

    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    run()
