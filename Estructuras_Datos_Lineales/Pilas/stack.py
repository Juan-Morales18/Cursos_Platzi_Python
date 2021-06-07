from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return "The stack is empty"

    def peek(self):
        """
        Obtener valor en top
        """
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        while self.top:
            self.pop()

    def clear_alternative(self):
        self.top = None
        self.size = 0

    def search_item(self, data):
        probe = self.top

        while probe != None and probe.data != data:
            probe = probe.next

        if probe != None:
            return f"{data} was founded"
        else:
            return f"{data} is not in the stack"

    def iter(self):
        probe = self.top

        while probe:
            yield probe.data
            probe = probe.next
