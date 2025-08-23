# When replacing with slices, the replacement must match the step.

lst = [0, 1, 2, 3, 4, 5]

lst[::2] = [10, 20, 30]
print(lst)   # [10, 1, 20, 3, 30, 5]

# lst[::2] = [99, 100] → ERROR: mismatch in element count
