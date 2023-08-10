class Vehicle:
    def __init__(self, max_speed_):
        self.max_speed = max_speed_

    def __str__(self):
        return f"Max Speed: {self.max_speed}"



class Tram(Vehicle):
    def __init__(self, max_speed_, vehicle_number_, tram_depot_place_, tram_length_):
        super().__init__(max_speed_)
        self.vehicle_number = vehicle_number_
        self.tram_depot_place = tram_depot_place_
        self.tram_length = tram_length_

    def __str__(self):
        return f"Tram: Vehicle Number: {self.vehicle_number}, Depot Place: {self.tram_depot_place}," \
               f" Tram Length: {self.tram_length}, {super().__str__()}"


class Bus(Vehicle):
    def __init__(self, max_speed_, vehicle_number_, bus_depot_place_, monthly_fuel_consumption_):
        super().__init__(max_speed_)
        self.vehicle_number = vehicle_number_
        self.bus_depot_place = bus_depot_place_
        self.monthly_fuel_consumption = monthly_fuel_consumption_

    def __str__(self):
        return f"Bus: Vehicle Number: {self.vehicle_number}, Depot Place: {self.bus_depot_place}," \
               f" Monthly Fuel Consumption: {self.monthly_fuel_consumption}, {super().__str__()}"

class Depot:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add(self, vehicle):
        self.vehicles.append(vehicle)

    def __str__(self):
        vehicles_info = "\n".join(str(vehicle) for vehicle in self.vehicles)
        return vehicles_info

class TramDepot(Depot):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Tram Depot: Name: {self.name}\n{super().__str__()}"

    def calculate_no_of_trams(self):
        pass


class BusDepot:
    def __init__(self, name_):
        self.name = name_
        self.buses = []

    def add_bus(self, bus):
        self.buses.append(bus)

    def __str__(self):
        buses_info = "\n".join(str(bus) for bus in self.buses)
        return f"Bus Depot: Name: {self.name}\n{buses_info}"

    def calculate_fuel_usage(self):
        pass

def main():

    tram1 = Tram(max_speed_=70, vehicle_number_='TR001', tram_depot_place_='Depot 1', tram_length_=30)
    bus1 = Bus(max_speed_=90, vehicle_number_='BUS001', bus_depot_place_='Depot 2', monthly_fuel_consumption_=500)

    tram_depot = TramDepot(name_='Tram Depot 1')
    bus_depot = BusDepot(name_='Bus Depot 1')

    tram_depot.add_tram(tram1)
    bus_depot.add_bus(bus1)

    print(tram_depot)
    print(bus_depot)


if __name__ == "__main__":
    main()
