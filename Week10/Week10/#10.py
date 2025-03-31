#10 replace spaces with underscores and vice versa
import re
def find_location(text, word):
    match = re.search(word, text)
    if match:
        return match.start(), match.end()
    return None

print(find_location("The quick brown fox...", "fox"))

