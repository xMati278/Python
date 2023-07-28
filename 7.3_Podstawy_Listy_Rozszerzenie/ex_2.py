import sys
import random

numbers = str(input("Enter numbers separated by a space: "))
allowedCharList = [' ', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for char in numbers:
    if char not in allowedCharList:
        print("You have not entered the correct values.")
        sys.exit(1)

correctNumbers = numbers.split(" ")

for i in range(len(correctNumbers)):
    correctNumbers[i] = int(correctNumbers[i])

# correct_numbers = []
# for num in numbers.split(" "):
#     correct_numbers.append(int(num))
#

for i in range(len(correctNumbers)):
    if correctNumbers[i] < 1 or correctNumbers[i] > 49:
        print(f'The number {correctNumbers[i]} was incorrect and ', end="")
        correctNumbers[i] = random.randint(1, 49)
        print(f'was replaced with the value {correctNumbers[i]}')




print(correctNumbers)