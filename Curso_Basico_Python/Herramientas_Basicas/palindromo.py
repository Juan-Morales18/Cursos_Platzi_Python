def is_palindrome(word):

    word = word.replace(' ', '')
    word = word.lower()

    if word == word[::-1]:
        return True
    else:
        return False


def run():
    word = input("Ingrese una palabra: ")

    result = is_palindrome(word)

    if result == True:
        print(f"La palabra '{word}' es palindroma ")
    else:
        print(f"La palabra '{word}' no es palindroma")


if __name__ == '__main__':
    run()
