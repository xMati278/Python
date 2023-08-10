def product_of_numbers(*args: int):
    result = 1
    for number in args:
        result *= number
    return result


print(product_of_numbers(15, 12 ,2))
