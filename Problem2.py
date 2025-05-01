class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone, emergency_contact_name, emergency_contact_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone = phone
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone

    # Accessors
    def get_full_name(self):
        return f"{self.__first_name} {self.__middle_name} {self.__last_name}"

    def get_address(self):
        return f"{self.__address}, {self.__city}, {self.__state} {self.__zip_code}"

    def get_phone(self):
        return self.__phone

    def get_emergency_contact(self):
        return f"{self.__emergency_contact_name} - {self.__emergency_contact_phone}"

    # Mutators (not shown for brevity but can be added)

    def display_info(self):
        print("Patient Information")
        print("-------------------")
        print("Name:", self.get_full_name())
        print("Address:", self.get_address())
        print("Phone:", self.get_phone())
        print("Emergency Contact:", self.get_emergency_contact())
        print()


class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    # Accessors
    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charge(self):
        return self.__charge

    def display_info(self):
        print("Procedure:", self.__name)
        print("Date:", self.__date)
        print("Practitioner:", self.__practitioner)
        print(f"Charge: ${self.__charge:.2f}")
        print()


# Main Program
def main():
    # Create Patient
    patient = Patient(
        first_name="Jane",
        middle_name="Marie",
        last_name="Doe",
        address="123 Health St",
        city="Wellness",
        state="IL",
        zip_code="60123",
        phone="555-123-4567",
        emergency_contact_name="John Doe",
        emergency_contact_phone="555-765-4321"
    )

    # Create Procedures
    procedure1 = Procedure("X-ray", "04/30/2025", "Dr. Smith", 250.00)
    procedure2 = Procedure("Blood Test", "04/30/2025", "Nurse Allen", 150.00)
    procedure3 = Procedure("MRI Scan", "04/30/2025", "Dr. Johnson", 1200.00)

    # Display Patient Info
    patient.display_info()

    # Display Procedures and Total Cost
    print("Procedures")
    print("----------")
    procedure1.display_info()
    procedure2.display_info()
    procedure3.display_info()

    total = procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()
    print(f"Total Charges: ${total:.2f}")


# Run the program
main()

