def calculate_area(length, width, shape):
    if shape == "triangle":
        return (1/2) * length * width
    elif shape == "rectangle":
        return length * width
    else:
        return "Invalid shape type. Use 'triangle' or 'rectangle'."

# Ask user to enter details:
length = float(input("Enter length: "))
width = float(input("Enter width: "))
shape = input("Enter shape type (triangle/rectangle): ").lower()

print(calculate_area(length, width, shape))

def test_calculate_area():
    # Test cases: (length, width, shape, expected_output)
    test_cases = [
        (5, 3, "rectangle", 15),
        (4, 6, "triangle", 12),
        (2, 2, "rectangle", 4),
        (3, 4, "triangle", 6),
        (1, 1, "circle", "Invalid shape type. Use 'triangle' or 'rectangle'."),
    ]

    for length, width, shape, expected in test_cases:
        result = calculate_area(length, width, shape)
        assert result == expected, f"Failed for {length}, {width}, {shape}. Expected {expected}, got {result}"

    print("All test cases passed!")

# Run the tests
test_calculate_area()
