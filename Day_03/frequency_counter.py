# Dictionaries & Sets
# Count word frequency in a string
# Python
# .get(key, default) avoids KeyErrors

import re

text = "To be, or not to be—that is the question."

# tokenize: words and simple contractions

words = re.findall(r"\b\w+'\w+|\b\w+\b", text.lower())

frequency = {}
for w in words:
    frequency[w] = frequency.get(w, 0) + 1

print((frequency))
