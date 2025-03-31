#5 mstch word at the beginning of a string
import re
def starts_with_word(text):
    return bool(re.match(r'^\w+', text))

print(starts_with_word("The quick brown fox..."))     # ✅
print(starts_with_word(" The quick brown fox..."))    # ❌ (starts with space)

