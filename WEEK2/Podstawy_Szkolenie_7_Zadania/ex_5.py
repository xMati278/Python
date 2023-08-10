def mix_even_and_odd_numbers(**kwargs):
    even_numbers_list = kwargs.get('even', [])
    odd_numbers_list = kwargs.get('odd', [])
    mix_numbers_list = []

    # for i in range(max(len(even_numbers_list), len(odd_numbers_list))):
    #
    #     if odd_numbers_list:
    #         mix_numbers_list.append(odd_numbers_list.pop(0))
    #
    #     if even_numbers_list:
    #         mix_numbers_list.append((even_numbers_list.pop(0)))

    for even, odd in zip(even_numbers_list, odd_numbers_list):
        mix_numbers_list.append(even)
        mix_numbers_list.append(odd)

    return mix_numbers_list


even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]

print(mix_even_and_odd_numbers(even=even_numbers, odd=odd_numbers))
