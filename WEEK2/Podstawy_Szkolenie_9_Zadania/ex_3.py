class Rectangle:
    def __init__(self, width_, length_):
        self.length = length_
        self.width = width_

    def figure_field(self):
        print(f'Figure field: {self.length* self.width}')

    def figure_perimeter(self):
        print(f'Figure perimeter: {2* (self.width+ self.length)}')


def main():
    figure = Rectangle(5, 10)
    figure.figure_field()
    figure.figure_perimeter()


if __name__ == "__main__":
    main()
