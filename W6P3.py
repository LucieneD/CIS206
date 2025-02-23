
def encode(text):
    if not text:  # Handle empty input
        return "Error: Input cannot be empty."

    encoded_text = "##00" 
    count = 1

    for i in range(1, len(text)):  # Loop through text
        if text[i] == text[i - 1]:  
            count += 1
        else:
            encoded_text += escape_character(text[i - 1], count)  
            count = 1  # Reset count

    encoded_text += escape_character(text[-1], count)
    return encoded_text


def escape_character(char, count):
   
    if char == "#":
        char = "##"

    if char.isdigit():
        char = f"#{char}" 

    return char + (str(count) if count > 1 else "")


def decode(rle_text):
    if not rle_text.startswith("##00"):  # Check encoding marker
        return encode(rle_text)  # If not encoded, encode it first

    decoded_text = ""
    i = 4  # Start after `##00`

    while i < len(rle_text):
        char = rle_text[i]
        count = ""

        if char == "#" and i + 1 < len(rle_text): 
            next_char = rle_text[i + 1]

            if next_char == "#": 
                decoded_text += "#"
                i += 2  # Skip both #
                continue
            elif next_char.isdigit(): 
                decoded_text += next_char
                i += 2  # Skip both # and the digit
                continue

        i += 1 
        while i < len(rle_text) and rle_text[i].isdigit():  # Read count
            count += rle_text[i]
            i += 1

        decoded_text += char * (int(count) if count else 1)
    return decoded_text


def main():
  
    user_input = input("Enter a string: ").strip()

    if user_input.startswith("##00"):
        result = decode(user_input)
        print("Decoded string:", result)
    else:
        result = encode(user_input)
        print("Encoded string:", result)


if __name__ == "__main__":
    main()
