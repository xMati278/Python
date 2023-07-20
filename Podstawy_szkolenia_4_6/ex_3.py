list=[]

for i in range (10):
    number= int(input(f'Enter number no.{i+1}: '))
    list.append(number)

for j in list:
    if j%2 == 0:
        print (j)
    else:
        continue