dict = {}
weatherList = []

while 1:
    weather = str(input("Enter the city and rainfall total separated by a space:"))
    if weather != "":
        weatherList = weather.split(" ")

        if weatherList[0] not in dict.keys():
            dict[weatherList[0]] = int(weatherList[1])
        else:
            dict[weatherList[0]] = dict.get(weatherList[0]) + int(weatherList[1])
    else:
        break

for key, value in dict.items():
    print(f'{key}: {value}')
