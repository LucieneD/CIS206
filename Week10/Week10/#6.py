#6 match word containing Z
import re
def word_with_z(text):
    return re.findall(r'\b\w*z\w*\b', text)

print(word_with_z("The quick brown fox jumps over the lazy dog."))
print(word_with_z("Python Exercises."))

