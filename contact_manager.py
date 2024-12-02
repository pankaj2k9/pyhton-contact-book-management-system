from utils import validate_name, validate_phone

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ").strip()
        if not validate_name(name):
            print("Error: Name must be a string.")
            return

        phone = input("Enter phone number: ").strip()
        if not validate_phone(phone):
            print("Error: Phone number must be an integer.")
            return

        if phone in self.contacts:
            print("Error: Phone number already exists.")
            return

        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        self.contacts[phone] = {"name": name, "email": email, "address": address}
        print(f"Contact for {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        for phone, details in self.contacts.items():
            print(f"{details['name']} - {phone} - {details['email']} - {details['address']}")

    def remove_contact(self):
        phone = input("Enter the phone number to delete: ").strip()
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact removed successfully!")
        else:
            print("Contact not found.")

    def search_contact(self):
        query = input("Enter name, phone, or email to search: ").strip()
        for phone, details in self.contacts.items():
            if query in (details['name'], phone, details['email']):
                print(f"Found: {details['name']} - {phone} - {details['email']} - {details['address']}")
                return
        print("No contact found.")
