import random

pesel = {'50030478561': {'kolor_oczu': 'niebieski','imie':'Jan','nazwisko':'Kowalski','wiek':'33'},
'16220678179': {'kolor_oczu': 'brązowy','imie':'Zbigniew','nazwisko':'Biały','wiek':'15'},
'82042434429': {'kolor_oczu': 'niebieski','imie':'Kazimierz','nazwisko':'Wielki','wiek':'56'},
'53081352991': {'kolor_oczu': 'szary','imie':'Kacper','nazwisko':'Szybki','wiek':'25'},
'54081198637': {'kolor_oczu': 'zielony','imie':'Anna','nazwisko':'Luźny','wiek':'43'}
        }
names= ["Ada", "Amelia", "Anna", "Balbina", "Dagmara", "Ilona", "Inga", "Krystyna"]
keys_to_remove = []



for key, value in pesel.items():
    value['imie_matki']= random.choice(names)



for peselKey, valueKey in pesel.items():
    if peselKey[-1] == '1':
        keys_to_remove.append(peselKey)

for x in keys_to_remove:
    pesel.pop(x)



for printKey, printValue in pesel.items():
    print(f'Pesel: {printKey}')

    for printKeyInfo, printValueInfo in printValue.items():
        print(f'    {printKeyInfo}: {printValueInfo}')
    print()