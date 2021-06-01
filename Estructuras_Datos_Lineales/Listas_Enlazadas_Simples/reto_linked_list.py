from linked_list import SinglyLinkedList
from array_ import Array


def main():
    print("\nCreating an array...")
    array = Array(5)
    print(f"Array length: {array.__len__()}")
    array.sequential_fill(5)

    print(f"Array values: {array.__str__()}")

    print("\nAdding array values to a singly linked list...")
    list_values = SinglyLinkedList()

    for element in array:
        list_values.append(element)

    print("\nList Values: ")
    print(list_values.print_())


if __name__ == "__main__":
    main()
