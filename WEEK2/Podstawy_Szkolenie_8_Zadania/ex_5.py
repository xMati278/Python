with open("ex_5_przyklad.txt", encoding="utf-8") as plik:
    plik.tell() #zwraca pozycję kursora
    plik.seek(43) #przesuwa kursor na podaną pozycję
    print(plik.read(1)) # odczytuje i drukuje 1 bajt pozycji kursora w pliku


#Wynik to: o