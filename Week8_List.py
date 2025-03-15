
# Function to load customer data from a text file
def load_customers(filename):
    customers =load_customers [""northwind.txt"]
    with open(northwind.txt, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('|') 
            if len(parts) >= 3:  # Ensuring enough data points exist
                customer_id, company_name, contact_name = parts[:3]
                customers.append((customer_id, company_name, contact_name))  # Store as tuple
    return customers

# Function to display customers sorted by company name
def display_by_company(customers):
    sorted_customers = sorted(customers, key=lambda x: x[1])  # Sort by company name
    for customer in sorted_customers:
        print(f"{customer[0]} - {customer[1]} - {customer[2]}")

# Function to display customers sorted by contact name
def display_by_contact(customers):
    sorted_customers = sorted(customers, key=lambda x: x[2])  # Sort by contact name
    for customer in sorted_customers:
        print(f"{customer[0]} - {customer[1]} - {customer[2]}")

# Function to search for a customer by company name
def search_by_company(customers, search_name):
    results = [customer for customer in customers if search_name.lower() in customer[1].lower()]
    if results:
        for customer in results:
            print(f"{customer[0]} - {customer[1]} - {customer[2]}")
    else:
        print("No matching customers found.")

# Function to search for a customer by contact name
def search_by_contact(customers, search_name):
    results = [customer for customer in customers if search_name.lower() in customer[2].lower()]
    if results:
        for customer in results:
            print(f"{customer[0]} - {customer[1]} - {customer[2]}")
    else:
        print("No matching customers found.")

# Function to display the menu and handle user input
def menu():
    filename = "northwind_customers.txt"  # Ensure this file exists with data
    customers = load_customers(filename)

    while True:
        print("\nMenu:")
        print("1. Display customers sorted by company name")
        print("2. Display customers sorted by contact name")
        print("3. Search customers by company name")
        print("4. Search customers by contact name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_by_company(customers)
        elif choice == "2":
            display_by_contact(customers)
        elif choice == "3":
            search_name = input("Enter company name to search: ")
            search_by_company(customers, search_name)
        elif choice == "4":
            search_name = input("Enter contact name to search: ")
            search_by_contact(customers, search_name)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
