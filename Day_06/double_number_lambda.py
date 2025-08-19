# The lambda lambda x: x * 2 is a concise way to create a function that doubles its input.

double = lambda x: x * 2

# Using the function as is
print(double(5))  # Output: 10
print(double(10)) # Output: 20

# Assigning a variable to the function
number_to_double = int(input("Enetr number to double"))
print("The number you entered is ", double(number_to_double), " when doubled")
