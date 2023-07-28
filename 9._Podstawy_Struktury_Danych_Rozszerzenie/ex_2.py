import random

numberSet = set()
toRemove = set()

for i in range(15):
    numberSet.add(random.randint(5, 120))

print(f'Before: {numberSet}')

for number in numberSet:
    if number % 2 == 0:
        toRemove.add(number)

for x in toRemove:
    numberSet.discard(x)

print(f'After: {numberSet}')