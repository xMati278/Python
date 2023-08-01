family = ['Adam', 'Stanisław', 'Joanna', 'Kornelia', 'Kacper']

for i in range(len(family)):
    for j in range(i+1 ,len(family)):
        print(f'{family[i]} - {family[j]}')