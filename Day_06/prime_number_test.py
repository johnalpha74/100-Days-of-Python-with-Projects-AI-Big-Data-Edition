def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    # Test cases: (input, expected_output)
    test_cases = [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (25, False),
        (29, True),
        (30, False),
        (31, True),
        (100, False),
    ]

    for number, expected in test_cases:
        result = is_prime(number)
        assert result == expected, f"Failed for {number}. Expected {expected}, got {result}"

    print("All test cases passed!")

# Run the tests
test_is_prime()
