def find_max_number(number_list):
    highest_number_index = 0

    for index, element in enumerate(number_list):
        if element > number_list[highest_number_index]:
            highest_number_index = index

    return highest_number_index

nums = [4, 6, 8, 24, 12, 2]

print(find_max_number(nums))