plik = open("ex_2_przyklad.txt", "r")
linie = plik.readlines()
print(linie)


plik.close() # W zadaniu brakowało tej linni kodu, czyli zamknięcia pliku na którym pracujemy