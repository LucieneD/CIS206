import csv
import urllib.request

csv_url = "https://raw.githubusercontent.com/tmcnab/northwind-mongo/master/customers.csv"

def load_customers(url):
    """Fetches CSV data from the URL and returns a list of dictionaries."""
    with urllib.request.urlopen(url) as response:
        return list(csv.DictReader(map(bytes.decode, response)))

def display_customers(customers, fields):
    """Prints selected fields for each customer."""
    for c in customers:
        print(", ".join(f"{field}: {c[field]}" for field in fields))
    print("-" * 50)  # Corrected indentation

def sort_customers(customers, key):
    """Sorts the list of customers by a given key."""
    return sorted(customers, key=lambda x: x[key])

def search_customers(customers, key, term):
    """Searches customers by key (CompanyName or ContactName)."""
    term = term.lower()
    return [c for c in customers if term in c[key].lower()]

def main():
    customers = load_customers(csv_url)

    while True:
        print("\n1. Sort by Company Name\n2. Sort by Contact Name\n3. Search Company\n4. Search Contact\n5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_customers(sort_customers(customers, "CompanyName"), ["CompanyName", "ContactName", "Phone"])
        elif choice == "2":
            display_customers(sort_customers(customers, "ContactName"), ["ContactName", "CompanyName", "Phone"])
        elif choice == "3":
            term = input("Enter company name: ").strip()
            display_customers(search_customers(customers, "CompanyName", term), ["CompanyName", "ContactName", "Phone"])
        elif choice == "4":
            term = input("Enter contact name: ").strip()
            display_customers(search_customers(customers, "ContactName", term), ["ContactName", "CompanyName", "Phone"])
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
