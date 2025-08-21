# A slice extracts a portion of a list using the syntax

# Exercise one:

numbers = [1, 6, 7, 8, 78, 65, 33]
print(numbers[1:3])                 # [6, 7]
print(numbers[2:7])                 # [6, 7, 8, 78, 65, 33]
print(numbers[2:])                  # [6, 7, 8, 78, 65, 33]
print(numbers[1::2])                # [6, 8, 65]
print(numbers[::2])                 # [1, 7, 78, 33]
print(numbers[::3])                 # [1, 8, 33]
print(numbers[::1])                 # [1, 6, 7, 8, 78, 65, 33]



