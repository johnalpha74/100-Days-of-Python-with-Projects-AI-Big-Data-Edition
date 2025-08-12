# Print numbers from 1 to 100 with the following rules:
# If a number is divisible by 3, print "Fizz"
# If a number is divisible by 5, print "Buzz"
# If a number is divisible by both 3 and 5, print "FizzBuzz"
# Otherwise, print the number itself

for i in range(1, 101):
    if 1 % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
else: print(i)
