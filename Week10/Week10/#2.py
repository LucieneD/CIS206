#program that matches a string that has an A followed by zero or more B's
import re
def match_ab(string):
    return bool(re.fullmatch(r'ab*', string))

tests= ["ab", "abc", "a", "ab", "abb"]
for t in tests:
    print(f"{t}: {match_ab(t)}")
