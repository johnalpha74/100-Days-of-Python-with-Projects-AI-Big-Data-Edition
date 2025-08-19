# Define a reusable greet function
# The greet function takes a name and an optional greeting (defaulting to "Hello").

def greet(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"

# Use the function as is
print(greet("Alice"))          # Output: Hello, Alice!
print(greet("Bob", "Hi"))      # Output: Hi, Bob!

# Ask user to enter a name
name = input("Please enter you name: ")
print("Hello " + name.capitalize())
