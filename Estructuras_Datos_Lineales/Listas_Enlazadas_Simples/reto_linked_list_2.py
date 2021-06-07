
from node import Node


class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):

        node = Node(data, None)

        if self.head == None:
            self.head = node
        else:
            probe = self.head
            previous = self.head

            while probe:
                if probe.next == None:
                    previous.next = node
                    break
                previous = probe
                probe = probe.next

    def push(self, data):
        node = Node(data, None)

        if self.head == None:
            self.head = node
        else:
            probe = self.head

            previous = node
            previous.next = probe
            self.head = previous

    def insert_by_position(self, data, target_pos):
        probe = self.head
        previous = self.head

        try:
            if target_pos < 0 or target_pos > self.size_():
                print(f"Position {target_pos} is out of range")
                return
            if target_pos == 0:
                self.push(data)
            else:
                new_node = Node(data, None)
                index = 0

                while probe != None and index < target_pos:
                    previous = probe
                    probe = probe.next
                    index += 1
                previous.next = new_node
                new_node.next = probe

        except TypeError:
            print("The position must be an int")

    def display(self):
        probe = self.head
        result = ""

        while probe:
            result += str(probe.data)+""
            if probe.next != None:
                result += " --> "
            probe = probe.next
        return result

    def size_(self):

        probe = self.head
        size = 0

        while probe != None:
            probe = probe.next
            size += 1
        return size

    def search_by_value(self, target_value):
        probe = self.head

        while probe != None and probe.data != target_value:
            probe = probe.next
        if probe != None:
            return f"The value {target_value} was founded :)"
        else:
            return f"The value {target_value} was not founded :("

    def search_by_position(self, target_pos):
        probe = self.head
        index = 0

        try:
            if target_pos < 0 or target_pos > self.size_():
                return (f"Position {target_pos} is out of range")

            while probe and index < target_pos:
                probe = probe.next
                index += 1

            if probe != None:
                return f"The element in position {target_pos} is {probe.data}"

        except TypeError:
            return ("Position must be an int")

    def pop(self):
        probe = self.head
        self.head = probe.next

    def delete_tail(self):
        probe = self.head
        previous = self.head

        if probe == None:
            print("The list is empty")
            return
        if probe.next == None:
            self.pop()
        else:
            while probe:
                if probe.next == None:
                    previous.next = None
                    break
                previous = probe
                probe = probe.next

    def delete_by_position(self, target_pos):

        probe = self.head
        previous = None
        index = 0

        try:
            if target_pos < 0 or target_pos >= self.size_():
                print(f"The position {target_pos} is out of the range ")
                return
            if target_pos == 0:
                self.pop()
            elif target_pos == self.size_()-1:
                self.delete_tail()
            else:
                while probe:
                    if index == target_pos:
                        previous.next = probe.next
                    previous = probe
                    probe = probe.next
                    index += 1
        except TypeError:
            print("Position must be an int")

    def replace_value_by_position(self, target_pos, new_value):
        probe = self.head
        index = 0

        try:
            while probe != None and target_pos != index:
                probe = probe.next
                index += 1

            if target_pos == index and probe != None:
                probe.data = new_value
            else:
                print(f"Position {target_pos} is out of the range")
        except:
            print("Position must be an int")

    def replace(self, old_value, new_value):
        probe = self.head

        while probe != None and probe.data != old_value:
            probe = probe.next

        if probe != None:
            probe.data = new_value
            print(
                f"The value = {old_value} was replaced for new value = {new_value}")
        else:
            print(f"The value {old_value} is not in the list")
