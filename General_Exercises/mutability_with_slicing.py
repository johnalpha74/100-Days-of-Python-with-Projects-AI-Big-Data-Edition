# Slices can be used to replace portions of a list

numbers = [1, 2, 3, 4, 5]

numbers [1:4] = [99, 100]
print(numbers)   # [1, 99, 100, 5]

numbers[:2] = [7, 8, 9]
print(numbers)   # [7, 8, 9, 100, 5]

# delete slices

lst = [1, 2, 3, 4, 5]
del lst[1:3]
print(lst)   # [1, 4, 5]
