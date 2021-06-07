
from array_ import Array


class ArrayBasedStack():
    def __init__(self, size):
        self.size = size
        self.top = None
        self.arr = Array(self.size)

    def push(self, data):
        if self.top == None:
            self.arr.__setitem__(0, data)
            self.top = 0
        else:
            if self.top + 1 < self.size:
                new_top = self.top + 1
                self.arr.__setitem__(new_top, data)
                self.top = new_top
            else:
                print("The stack is full")

    def pop(self):
        if self.size == 0:
            print("The stack is empty")
        else:
            data = self.arr.__getitem__(self.top)
            self.arr.__setitem__(self.top, None)

            if self.top == 0:
                self.top == None
                self.size = 0
            else:
                self.top -= 1
                self.size -= 1
            print(f"The value {data} was poped")

    def clear(self):
        if self.size == 0:
            print("The stack is empty")
        else:
            for i in range(self.size):
                if i <= self.top:
                    self.arr.__setitem__(i, None)
                    self.size -= 1

    def search(self, data):
        i = 0
        while i <= self.top and self.arr[i] != data:
            i += 1
        if self.arr[i] == data:
            print(f"The value {data} was founded")
        else:
            print(f"The value {data} is not in the stack")

    def iter(self):

        index = self.top

        while index >= 0:
            yield self.arr.__getitem__(index)
            index -= 1
