
def encode(text):
    encoded_text= "" #store result
    count = 1 # start counting characters
    for i in range (1, len(text)): #loop through text
        if text[i] == text [i-1]:
            count += 1
        else:
            encoded_text+= text[i-1] + (str(count) if count > 1 else"")
            count = 1 
    encoded_text += text[-1] + (str(count) if count > 1 else "")
    
    return encoded_text
# Get user input and display result
user_input = input("Enter a word: ").strip()  # Get input from user
result = encode(user_input)  # Call the function
print("Encoded string:", result)  # Print the result