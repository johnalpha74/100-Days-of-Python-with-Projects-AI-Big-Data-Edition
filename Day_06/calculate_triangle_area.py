# Write a function called calculate_area that takes base and height as an input
# and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

# define the function
def calculate_area(base, height):
    area = (1/2) * base * height
    return area


# Ask user to enter the base and height
base = int(input("Please enter base of the triangle : "))
height = int(input("Please enter the height of the triangle : "))
print(calculate_area(base, height))
