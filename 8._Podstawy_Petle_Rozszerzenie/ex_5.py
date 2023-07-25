zamowienia = {"Klient_1335" : {"nazwa_potrawy" : "rosół", "ocena" : 5, "rachunek" : 20.0},
              "Klient_222" :{"nazwa_deseru" : "lody waniliowe", "rachunek" : 5.0 }}

for key, value in zamowienia.items():
    print(f'{key}: ')
    for dictKey, dictValue in value.items():
        print(f'{dictKey}: {dictValue}')
    print()