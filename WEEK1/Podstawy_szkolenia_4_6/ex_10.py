import random

min_no = int(input("Enter a min. value: "))
max_no = int(input("Enter a max. value: "))

points= max_no-min_no
randValue= random.randint(min_no, max_no)

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