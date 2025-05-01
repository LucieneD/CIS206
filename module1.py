import json

# Load JSON data
with open("books.json", "r") as file:
    books = json.load(file)

# Display all book data
print("Book Collection:")
for book in books:
    print(f"{book['title']} by {book['author']} ({book['year']})")

# Loop for user input
while True:
    title_input = input("\nEnter a book title (or type 'exit' to quit): ").strip()
    if title_input.lower() == 'exit':
        break

    found = False
    for book in books:
        if book["title"].lower() == title_input.lower():
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year Published: {book['year']}")
            found = True
            break
    if not found:
        print(f"\n'{title_input}' not found.")

