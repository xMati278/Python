weight = float(input("Enter your weight(in kg): "))
height = float(input("Enter your height(in m): "))

bmi = weight/pow(height,2)

if bmi<18.5:
    print("You are underweight.")
elif bmi<24:
    print('You are of normal weight.')
elif bmi<26.5:
    print("You are slightly overweight.")
elif bmi<30:
    print("You are overweight.")
elif bmi<35:
    print("You are 1st class obese.")
elif bmi<40:
    print("You are 2nd class obese.")
else:
    print("You are 3rd class obese.")