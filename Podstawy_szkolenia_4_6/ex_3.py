arr = []

for i in range (10):
    number = int(input(f'Enter number no.{i+1}: '))
    arr.append(number)

for j in arr:
    if j % 2 == 0:
        print(j)