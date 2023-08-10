from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError


class Sqaure(Shape):
    def __init__(self, length_):
        self.length = length_

    def calculate_area(self):
        return self.length ** 2


def main():
    shape = Shape()
    square = Sqaure(5)

    print("Area of a generic shape:", shape.calculate_area())
    print("Area of a square:", square.calculate_area())




if __name__ == "__main__":
    main()
