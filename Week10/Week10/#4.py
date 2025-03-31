#4 find sequences of lowercase letters joined by an underscore
import re
def find_lower_underscore(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)

print(find_lower_underscore("aab_cbbbc"))
print(find_lower_underscore("aab_Abbbc"))
print(find_lower_underscore("Aaab_abbbc"))

