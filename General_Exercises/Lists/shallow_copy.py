# shallow copy creates a new object, but does not recursively copy the objects found in the original object
import copy

# Creating shallow copy Using the copy Module

original_list = ["banana", "mango", "tomato", "guava", "orange", "passion", "grapes"]
shallow_copied_list = copy.copy(original_list)

print(shallow_copied_list)

# Using the list() Constructor or Slicing

shallow_copied_list = list(original_list)

# or
shallow_copied_list_new = original_list[:]

