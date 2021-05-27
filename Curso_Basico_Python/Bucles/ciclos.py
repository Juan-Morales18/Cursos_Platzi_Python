def run():
    LIMIT = 1000000
    num = 2
    exp = 0
    res = 1

    while res < LIMIT:
        print(f"{num}^{exp} = {res}")
        exp += 1
        res = num ** exp


if __name__ == '__main__':
    run()
