from stack import Stack


def run():
    stack = Stack()

    print(stack.size)

    stack.push('A')
    stack.push('B')
    stack.push('C')
    stack.push('D')

    print(stack.size)

    for i in stack.iter():
        print(i)

    print(stack.search_item('E'))

    stack.clear_alternative()
    print(stack.size)


if __name__ == '__main__':
    run()
