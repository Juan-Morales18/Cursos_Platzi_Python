from node import Node


def main():
    node3 = Node('C', None)
    node2 = Node('B', node3)
    node1 = Node('A', node2)

    print(
        f"Ref:{node1} Data:{node1.data} Next:{node1.next} --> Ref:{node2} Data:{node2.data} Next:{node2.next} --> Ref:{node3} Data:{node3.data} Next:{node3.next}")

    head = None

    for i in range(1, 5):
        head = Node(i, head)

    while head != None:
        print(head.data)
        head = head.next


if __name__ == '__main__':
    main()
