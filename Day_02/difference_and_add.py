# Given a = {1,2,3,4} and b = {3,4,5}, compute elements in a but not b, then add 10 to the set.

a = {1,2,3,4}
b = {3,4,5}

result = (a - b) | {10}
print(result)
