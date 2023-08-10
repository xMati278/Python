def rocket_setup():
    fuel = 0
    astronauts = 0

    while not fuel <= 5000 or fuel >= 30000:
        # if fuel <= 5000 or fuel >= 30000:
        fuel = int(input("Enter an initial amount of fuel between 5000 and 30000: "))
        # else:
        #     break

    while True:
        if astronauts <= 0 or astronauts >= 7:
            astronauts = int(input("Enter the number of astronauts between 1 and 7: "))
        else:
            break

    return fuel, astronauts


def rocket_flight(fuel_amount: int, astronauts_amount: int):
    height = 0
    flight_cost = 300 + (100 * astronauts_amount)
    while True:
        if fuel_amount >= flight_cost:
            fuel_amount -= flight_cost
            height += 100
        else:
            break

    return height


def orbit_check(distance: int):
    if distance > 2000:
        return "The spaceship has reached orbit."
    return "The spaceship failed to reach orbit."


fuel_in_tank, astronauts_on_board = rocket_setup()
distance_traveled = (rocket_flight(fuel_in_tank, astronauts_on_board))
print(f'The spaceship has reached an altitude of: {distance_traveled}')
orbit_check(distance_traveled)
