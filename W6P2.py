
def encode(text):
  
    encoded_text = ""
    count = 1  # Start counting characters

    for i in range(1, len(text)):  # Loop through text
        if text[i] == text[i - 1]:  # Check if consecutive characters match
            count += 1
        else:
            encoded_text += text[i - 1] + (str(count) if count > 1 else "")  # Add char & count if >1
            count = 1  # Reset count

    encoded_text += text[-1] + (str(count) if count > 1 else "")

    return encoded_text


def decode(rle_text):
    decoded_text = ""
    i = 0

    while i < len(rle_text):
        char = rle_text[i]  # Extract letter
        count = ""

        i += 1  
        while i < len(rle_text) and rle_text[i].isdigit():  # Check if it's a digit
            count += rle_text[i]
            i += 1
        decoded_text += char * (int(count) if count else 1)

    return decoded_text


def main():
    user_input = input("Enter a string: ").strip()

    if any(char.isdigit() for char in user_input):
        result = decode(user_input)
        print("Decoded string:", result)
    else: 
        result = encode(user_input)
        print("Encoded string:", result)


if __name__ == "__main__":
    main()
