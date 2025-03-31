#8 search for a literal string within a string
import re
def search_words(text, words):
    return [word for word in words if re.search(rf'\b{word}\b', text)]

sample = 'The quick brown fox jumps over the lazy dog.'
words = ['fox', 'dog', 'horse']
print(search_words(sample, words))

