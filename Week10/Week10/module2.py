#remove multiple spaces
import re
def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text)

print(remove_extra_spaces('Python      Exercises'))  # "Python Exercises"

