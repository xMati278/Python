class Vehicle:
    def __init__(self, mileage_, max_speed_):
        self.mileage = mileage_
        self.max_speed = max_speed_

    def add_mileage(self, mileage_amount):
        self.mileage += mileage_amount
        print(f'Current mileage: {self.mileage}')


def main():
    car_1 = Vehicle(100000, 250)
    car_1.add_mileage(150.5)


if __name__ == "__main__":
    main()
