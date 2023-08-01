colors = [ 'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy',
           'niebieski', 'czarny', 'czarny', 'zielony',
           'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']

colorsLen = len(colors)
print(f'Oryginalna lista kolorów zawiera: {colorsLen} elementów')
print()


setColors = set(colors)
setColorsLen = len(setColors)
print(f'Użyto {setColorsLen} różnych kolorów')
print()


for i in setColors:
    print(i)
print()


setColors = setColors | {"kolorowy"}
print(setColors)


setColors.discard("czarny")
print(setColors)