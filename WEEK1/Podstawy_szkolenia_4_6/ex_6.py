a = [3, 1, 5, 7, 9, 2, 6]

print(a[3]) # value with index 3
print(a[1:4]) # value between indexes 1 and 4
print(a[3:]) # values starting from index 3
print(a[-3:]) # values from last 3 indexes
print(a[:3]) # values from first 3 indexes
print(a[3:-1]) # values starting from index 3 without last value
print(a[::2]) # jump every two indexes
print(a[5:2:-1]) # return values from index between 2 and 5 and result is reversed
print(sum(a)) # return sum of list a
print(8 in a) # return True if 8 is in list a or return False if 8 is not in list a
print(4 not in a) #return True if 4 is not in list a or return False if 4 is in list a