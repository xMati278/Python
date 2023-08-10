import random
import datetime


def generate_values(amount: int) -> list:
    values = []
    for i in range(amount):
        value = random.randint(0, 999999)
        values.append(value)
    return values


def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


elem1000 = generate_values(1000)
elem10000 = generate_values(10000)
elem100000 = generate_values(100000)
elem1000000 = generate_values(1000000)

lists = [elem1000, elem10000, elem100000, elem1000000]
functions = [bubble_sort, insertion_sort, quick_sort]

with open('result.txt', 'w') as file:
    for function in functions:
        for data in lists:
            sort_start = datetime.datetime.now()

            result = function(data)

            sort_stop = datetime.datetime.now()
            sort_time = sort_stop - sort_start
            print(f'{function.__name__}, elements: {len(data)}, time: {sort_time}\n')
            file.write(f'{function.__name__}, elements: {len(data)}, time: {sort_time}\n')
