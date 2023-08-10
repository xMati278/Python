def fizz_buzz(number: int):

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


print(fizz_buzz(6))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(4))
