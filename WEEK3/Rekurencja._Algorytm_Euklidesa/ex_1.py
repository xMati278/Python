import random


def recursive_display(list_to_display, index=0):
    if index >= len(list_to_display):
        return 1
    else:
        print(list_to_display[index])
        recursive_display(list_to_display, index+1)


number_list = []
for i in range(15):
    number_list.append(random.randint(0, 9999))

recursive_display(number_list)
