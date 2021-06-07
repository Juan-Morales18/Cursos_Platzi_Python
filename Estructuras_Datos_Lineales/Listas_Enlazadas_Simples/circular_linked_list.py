from node import Node
from node import TwoWayNode


class Doubly_Circular_Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = TwoWayNode(data)

        if self.head == None:
            self.head = node
            self.head.next = self.head
            self.head.previous = self.head
            self.tail = self.head
        else:
            probe = self.head

            while probe.next != self.head:
                probe = probe.next

            probe.next = node
            node.previous = probe
            node.next = self.head
            self.tail = node
            self.head.previous = self.tail

    def size_(self):
        probe = self.head
        size = 0

        while probe:
            size += 1
            if probe.next == self.head:
                break
            probe = probe.next

        return size

    def display(self):
        result = ""
        probe = self.head

        count = 0

        while True:
            result += probe.data
            if probe.next == self.head:
                count += 1
                if count == 3:
                    break
                result += " ==> "
            else:
                result += "-->"
            probe = probe.next
        return result

    def display_in_reverse(self):
        result = ""
        probe = self.tail
        count = 0

        while True:
            result += probe.data
            if probe.previous == self.tail:
                count += 1
                if count == 3:
                    break
                result += " ==> "
            else:
                result += "-->"
            probe = probe.previous
        return result

    def push(self, data):
        temp = self.head
        new_node = TwoWayNode(data, self.tail, temp)
        temp.previous = new_node
        self.head = new_node
        self.tail.next = self.head

    def insert_by_position(self, target_pos, value):

        node = TwoWayNode(value)
        try:
            if target_pos >= 0:
                if target_pos == 0:
                    self.push(value)
                    return
                if target_pos == self.size_():
                    self.append(value)
                else:
                    probe = self.head
                    previous = None
                    index = 0

                    while probe.next != self.head and index < target_pos:
                        previous = probe
                        probe = probe.next
                        index += 1

                    if index == target_pos:
                        node = TwoWayNode(value, previous, probe)
                        previous.next = node
                        probe.previous = node
                    else:
                        print(f"Position {target_pos} is out of the range")
            else:
                if target_pos == -1:
                    self.append(value)
                elif target_pos == (self.size_()*(-1) - 1):
                    self.push(value)
                else:
                    probe = self.tail
                    node_previous = None
                    index = -1

                    while probe.previous != self.tail and index > target_pos:
                        node_previous = probe
                        probe = probe.previous
                        index -= 1
                    if index == target_pos:
                        node = TwoWayNode(value, probe, node_previous)
                        node_previous.previous = node
                        probe.next = node
                    else:
                        print(f"Position {target_pos} is out of the range*")
        except TypeError:
            print("Position must be an int")

    def pop(self):

        if self.head == None:
            print("List is empty")
            return
        self.head = self.head.next
        self.tail.next = self.head
        self.head.previous = self.tail

    def delete_tail(self):
        if self.head == None:
            print("The list is empty")
        self.tail = self.tail.previous
        self.tail.next = self.head
        self.head.previous = self.tail
