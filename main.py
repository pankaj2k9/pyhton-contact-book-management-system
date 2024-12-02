from contact_manager import ContactManager
from file_handler import FileHandler

def main():
    manager = ContactManager()
    file_handler = FileHandler("contacts.csv")

    # Load contacts at startup
    manager.contacts = file_handler.load_contacts()

    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit (Save)")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.remove_contact()
        elif choice == '4':
            manager.search_contact()
        elif choice == '5':
            # Save contacts before exiting
            file_handler.save_contacts(manager.contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
