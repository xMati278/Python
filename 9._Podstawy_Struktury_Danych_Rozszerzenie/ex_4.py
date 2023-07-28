dictionary = {}
weatherList = []

while 1:
    weather = str(input("Enter the city and rainfall total separated by a space:"))
    if weather != "":
        city, rainfall = weather.split(" ")

        if city not in dictionary.keys():
            dictionary[city] = int(rainfall)
        else:
            # dictionary[city] = dictionary.get(city) + int(rainfall)
            dictionary[city] += int(rainfall)
    else:
        break

for key, value in dictionary.items():
    print(f'{key}: {value}')
