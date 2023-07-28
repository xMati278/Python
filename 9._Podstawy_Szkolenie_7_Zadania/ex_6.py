import random


def filter_the_list(number_list):
    filtered_numbers = []

    for j in number_list:
        if 9 < j < 100:
            filtered_numbers.append(j)

    return filtered_numbers


value_list = []

for i in range(10):
    value_list.append(random.randint(1, 200))

print(filter_the_list(value_list))
