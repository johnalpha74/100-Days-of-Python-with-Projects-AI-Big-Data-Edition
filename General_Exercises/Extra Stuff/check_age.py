# if else if in python to check age

age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif age < 18:
    print("You are a minor")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior citizen")