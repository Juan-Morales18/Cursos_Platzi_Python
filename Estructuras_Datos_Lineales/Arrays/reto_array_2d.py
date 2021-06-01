

from array_ import Array
from random import randint


class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)

        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return str(result)

    def fill_slots_randomly(self, min=0, max=100):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] = randint(min, max)

    def fill_slots_sequently(self, start=0):
        value = start

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] = value
                value += 1


def main():
    matrix = Grid(3, 3)

    print(matrix.__str__())

    print(matrix.__getitem__(0)[2])

    print(matrix.get_height())

    print(matrix.get_width())

    for row in range(matrix.get_height()):
        for col in range(matrix.get_width()):
            matrix[row][col] = row * col

    print(matrix)

    print(matrix.__getitem__(2)[2])
    print(matrix.__str__())

    matrix.fill_slots_randomly()

    print(matrix.__str__())

    matrix.fill_slots_sequently(10)

    print(matrix.__str__())


if __name__ == '__main__':
    main()
