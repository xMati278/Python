lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, '2'] 

print(lista1,lista2,lista3)
print()

print(f'The first element of the list: {lista1[0]} and the fourth element of the list: {lista1[3]}')
print()

lista2[1] = lista3[1]
print(lista2)
print()

lista3[2] = str(input("Enter a text value for the 3rd element of lista3: "))
print()
print(lista3)
print()

lista1.append("słowo")
print(lista1)
print()

lista1.pop(2)
print(lista1)
print()

print(f'Number of elements lista3: {len(lista3)}')
print()

lista1 = lista1 + lista3
print(lista1)
print()