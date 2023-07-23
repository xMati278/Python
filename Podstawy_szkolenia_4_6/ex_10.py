import random

min= int(input("Enter a min. value: "))
max= int(input("Enter a max. value: "))

points= max-min
randValue= random.randint(min,max)

while 1:
    attempt = int(input("Enter a number: "))
    if randValue == attempt:
        print("You won!")
        print(f'Congratulations! You have earned {points} points')
        break
    elif randValue > attempt:
        print("You entered too low a number.")
        points -= 1
    else:
        print("You entered too high a number.")
        points -= 1