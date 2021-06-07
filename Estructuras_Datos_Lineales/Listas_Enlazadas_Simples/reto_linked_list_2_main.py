from reto_linked_list_2 import SinglyLinkedList


def list_operations(sl_list):
    elements = sl_list.display()
    size = sl_list.size_()
    print(size)
    print(elements)


def run():
    sl_list = SinglyLinkedList()

    print(sl_list)

    sl_list.append('A')
    elements = sl_list.display()

    sl_list.append('B')

    print(sl_list.search_by_value('B'))

    print(sl_list.search_by_position(6))

    sl_list.push('C')
    list_operations(sl_list)

    sl_list.insert_by_position('F', 1)
    list_operations(sl_list)

    sl_list.pop()
    list_operations(sl_list)

    sl_list.delete_tail()
    list_operations(sl_list)

    sl_list.delete_by_position(0)
    list_operations(sl_list)

    sl_list.insert_by_position('k', 1)
    sl_list.insert_by_position('l', 2)
    sl_list.insert_by_position('m', 3)
    sl_list.insert_by_position('n', 4)
    list_operations(sl_list)

    sl_list.delete_by_position(0)
    list_operations(sl_list)

    sl_list.replace_value_by_position(5, 'Juan')
    list_operations(sl_list)

    sl_list.replace('k', 'Am')
    list_operations(sl_list)


if __name__ == '__main__':
    run()
