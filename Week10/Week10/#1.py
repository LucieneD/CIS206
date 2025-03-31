#A program to check that a string contrains a certain set of characters
import re
def alphanumeric (string):
    return bool(re.fullmatch(r'[A-Za-z0-9]+', string))

print (alphanumeric("ABCDEFabcdef123450"))
print (alphanumeric("!@#$%^&*()"))