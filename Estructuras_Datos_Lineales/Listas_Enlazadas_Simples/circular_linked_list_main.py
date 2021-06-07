from circular_linked_list import Doubly_Circular_Linked_List


def run():
    dll = Doubly_Circular_Linked_List()

    print(dll)

    dll.append('A')

    print(dll.size_())

    dll.append('B')
    print(dll.size_())

    dll.append('S')
    print(dll.size_())

    dll.append('E')
    print(dll.size_())

    print(dll.head)

    elements = dll.display()
    print(elements)

    elements = dll.display_in_reverse()
    print(elements)

    dll.push('R')
    print(dll.size_())
    elements = dll.display()
    print(elements)

    dll.insert_by_position(6, 'Z')
    elements = dll.display()
    print(elements)

    dll.insert_by_position(-10, 'k')
    elements = dll.display()
    print(elements)

    dll.pop()
    elements = dll.display()
    print(elements)

    dll.delete_tail()
    elements = dll.display()
    print(elements)


if __name__ == '__main__':
    run()
