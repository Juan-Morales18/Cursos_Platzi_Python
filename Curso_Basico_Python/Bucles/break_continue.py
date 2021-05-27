def run():
    for i in range(1000):  # continue
        if i % 2 != 0:
            continue
        print(i)

    for i in range(100, 1000):  # break
        if i == 500:
            break
        print(i)


if __name__ == '__main__':
    run()
