from linked_list import SinglyLinkedList


def main():
    words = SinglyLinkedList()

    print(words)
    print(f"Size: {words.size}")
    print(f"Tail: {words.tail}")
    datas = words.print_()
    print(f"Datas: {datas}")

    words.append('Cat')
    print(f"Size: {words.size}")
    print(f"Tail: {words.tail}")
    datas = words.print_()
    print(f"Datas: {datas}")

    words.append('Gog')
    print(f"Size: {words.size}")
    print(f"Tail: {words.tail}")
    datas = words.print_()
    print(f"Datas: {datas}")

    words.append('Bull')
    print(f"Size: {words.size}")
    print(f"Tail: {words.tail}")
    datas = words.print_()
    print(f"Datas: {datas}")

    data_deleted = words.delete('Cat')
    print(data_deleted)
    print(f"Size: {words.size}")
    print(f"Tail: {words.tail}")
    datas = words.print_()
    print(f"Datas: {datas}")

    current = words.tail

    while current:
        print(current.data)
        current = current.next


if __name__ == '__main__':
    main()
