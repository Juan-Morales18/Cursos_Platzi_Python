from array_based_stack import ArrayBasedStack


def run():
    pila = ArrayBasedStack(5)

    print(pila.size)
    pila.push('A')
    pila.push('B')
    pila.push('C')
    pila.push('D')
    pila.push('E')
    pila.push('F')
    print(pila.size)
    pila.pop()
    print(pila.size)
    pila.search('E')
    print(pila.size)

    for i in pila.iter():
        print(i)


if __name__ == '__main__':
    run()
