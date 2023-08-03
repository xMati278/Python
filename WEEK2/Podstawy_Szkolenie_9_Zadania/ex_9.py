import datetime


class Tank:
    def __init__(self, name_, capacity_, liquid_amount_):
        self.name = name_
        self.capacity = capacity_
        self.liquid_amount = liquid_amount_
        self.operations = []

    def pour_water(self, volume):
        if (volume + self.liquid_amount) >= self.capacity:
            self.liquid_amount = self.capacity
        else:
            self.liquid_amount += volume

        print(f'{self.liquid_amount} liters were poured into {self.name}.')
        self.record_operation('pour_water', volume)

    def pour_out_water(self, volume):
        if volume > self.liquid_amount:
            self.liquid_amount = 0
        else:
            self.liquid_amount -= volume

        print(f'After pumping out {volume} liters from {self.name}, tank holds {self.liquid_amount}.')
        self.record_operation('pour_out_water', volume)

    def transfer_water(self, from_tank, volume):
        if volume > from_tank.liquid_amount:
            volume = from_tank.liquid_amount
        if (self.liquid_amount + volume) > self.capacity:
            volume = self.capacity - self.liquid_amount

        self.liquid_amount += volume
        from_tank.liquid_amount -= volume
        print(f'{volume} liters are transferred from tank {from_tank.name} to tank {self.name}.')
        self.record_operation('transfer_water', volume, from_tank.name)

    def record_operation(self, operation_name, volume, from_tank=None, success=True):
        operation = {
            'date_time': datetime.datetime.now(),
            'operation_name': operation_name,
            'volume': volume,
            'tank_name': self.name,
            'from_tank': from_tank,
            'success': success
        }
        self.operations.append(operation)

    def check_state(self):
        total_water = 0
        for operation in self.operations:
            if operation['operation_name'] == 'pour_water':
                total_water += operation['volume']
            elif operation['operation_name'] == 'pour_out_water':
                total_water -= operation['volume']
            elif operation['operation_name'] == 'transfer_water':
                total_water += operation['volume']
                if operation['from_tank'] == self.name:
                    total_water -= operation['volume']

        if total_water == self.liquid_amount:
            print("The state of the water is consistent.")
        else:
            print("The state of the water is not consistent.")


def find_largest_amount_of_liquid(tank_list):
    largest_amount_liquid = 0
    largest_amount_index = None
    for i in range(len(tank_list)):
        if tank_list[i].liquid_amount > largest_amount_liquid:
            largest_amount_liquid = tank_list[i].liquid_amount
            largest_amount_index = i

    print(f'Tank {tank_list[largest_amount_index].name} has the most liquid. Amount: {largest_amount_liquid} liters')


def find_most_full_tank(tank_list):
    most_filled_tank_percentage = 0
    most_filled_tank_index = None

    for i in range(len(tank_list)):
        fill_percent = (tank_list[i].liquid_amount / tank_list[i].capacity)

        if fill_percent > most_filled_tank_percentage:
            most_filled_tank_percentage = fill_percent
            most_filled_tank_index = i

    print(f'Tank {tank_list[most_filled_tank_index].name} has the most filled tank. Percent: '
          f'{most_filled_tank_percentage*100}. Amount: {tank_list[most_filled_tank_index].liquid_amount} liters')


def find_empty_tanks(tank_list):
    empty_tanks_list = []
    for i in range(len(tank_list)):
        if tank_list[i].liquid_amount == 0:
            empty_tanks_list.append(tank_list[i].name)
    print("Empty tanks list:", end=" ")
    for j in empty_tanks_list:
        print(f'"{j}"')


def main():
    tank_1 = Tank("Tankex 2000", 2000, 0)
    tank_2 = Tank("TopFuel XXL", 10000, 150)
    empty_tank = Tank("Poor reservoir", 100, 0)
    tank_list = [tank_1, tank_2, empty_tank]

    tank_1.pour_water(500)
    tank_1.pour_out_water(100)
    tank_1.transfer_water(tank_2, 100)

    find_largest_amount_of_liquid(tank_list)
    find_most_full_tank(tank_list)
    find_empty_tanks(tank_list)

    print(tank_1.operations)
    tank_1.check_state()


if __name__ == "__main__":
    main()
