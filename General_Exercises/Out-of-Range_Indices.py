# Python does not raise errors when slicing goes out of range.

lst = [1, 2, 3]

print(lst[0:10])   # [1, 2, 3] (stops at end safely)
print(lst[5:10])   # [] (empty list, no error)
