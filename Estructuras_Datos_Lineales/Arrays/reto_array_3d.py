from array_2d import Grid
from array_ import Array
from random import randint


class Cube():
    def __init__(self, rows, cols, depth, fill_value=None):
        self.cube = Grid(rows, cols)

        for row in range(rows):
            for col in range(cols):
                self.cube[row][col] = Array(depth, fill_value)

    def get_height(self):
        return self.cube.get_height()

    def get_width(self):
        return self.cube.get_width()

    def get_depth(self):
        return len(self.cube[0][0])

    def __getitem__(self, index):
        return self.cube[index]

    def __str__(self):
        result = ''

        for row in range(self.get_height()):
            result += "["
            for col in range(self.get_width()):
                result += "["
                for depth in range(self.get_depth()):
                    result += str(self.cube[row][col][depth]) + " "
                result += "]"
            result += "]" + "\n"

        return result

    def fill_cubes_randomly(self, min=0, max=100):

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    self.cube[row][col][depth] = randint(min, max)

    def fill_cubes_sequently(self, start):
        value = start

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    self.cube[row][col][depth] = value
                    value += 1


def main():
    cube = Cube(2, 2, 2)

    print(cube.__str__())

    cube.fill_cubes_sequently(1)

    print(cube.__str__())

    print(cube.__getitem__(1)[1][0])

    cube.fill_cubes_randomly()
    print(cube.__str__())


if __name__ == '__main__':
    main()
