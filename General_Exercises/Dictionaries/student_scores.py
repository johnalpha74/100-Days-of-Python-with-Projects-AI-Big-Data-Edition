# A dictionary is a key-value store.
# Keys must be immutable (strings, numbers, tuples), values can be any type

student_scores = {"Alice:85", "Evans: 60", "Rose:45"}

# Looping over .keys() explicitly

for name in student_scores.keys():
    print("Key:", name)
