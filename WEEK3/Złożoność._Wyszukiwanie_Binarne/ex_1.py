import random

random_list = [random.randint(0, 30) for _ in range(30)]
random_list.sort()


def binary_search_first_larger(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            if mid == 0 or arr[mid - 1] <= target:
                return mid
            else:
                right = mid - 1
        else:
            left = mid + 1
    return -1


position = binary_search_first_larger(random_list, 20)

if position != -1 and len(random_list) - position >= 10:
    result = "Yes, there are at least 10 numbers greater than 20."
else:
    result = "No, there are not at least 10 numbers greater than 20."

print("Generated list:", random_list)
print(result)
