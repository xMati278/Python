counter = {}
numberList = []

number = int(input("Enter a number: "))
number = str(number)

numbers = set(number)
numbers = sorted(numbers)

for i in numbers:
    counter[i] = number.count(i)

for key, value in counter.items():
    print(f'{key}: {value}')