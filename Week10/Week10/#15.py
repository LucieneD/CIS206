#find all words starting with a or e
import re
def words_a_e(text):
    return re.findall(r'\b[a|eA|E]\w*', text)

sample = "The following example creates an ArrayList..."
print(words_a_e(sample))

