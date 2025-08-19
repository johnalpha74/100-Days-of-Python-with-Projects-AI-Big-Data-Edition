# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area. Equation of rectangle's area is, rectangle area=length*width
# Equation of an area of a triangle is, area = (1/2)*base*height

# define the function
def calculate_area(length, width, shape):
    if shape == "triangle":
        return (1/2) * length * width
    if shape == "rectangle":
        return  length*width

    else:
        return "Invalid shape type. Use 'triangle' or 'rectangle'."


# Example usage:
length = float(input("Enter length: "))
width = float(input("Enter width: "))
shape = input("Enter shape type: ")
print(calculate_area(length, width, shape))



