# Contact Book Management System

A simple **Command Line Interface (CLI)** application to manage contacts, built in Python. This project allows users to **add, view, remove, search**, and **store contacts** in a persistent file. The program ensures data is loaded from and saved to a file automatically, making it reliable for basic contact management tasks.

---

## Features
- **Add Contacts**: Save contact details (name, phone number, email, and address).
- **View Contacts**: Display all saved contacts in a neat and organized format.
- **Remove Contacts**: Delete a contact by phone number.
- **Search Contacts**: Search for contacts by name, phone, or email.
- **File Persistence**: Contacts are saved in a `contacts.csv` file and loaded on startup.
- **Validation**: Ensures valid input for names, phone numbers, and email addresses.

---

## How It Works
1. At program startup:
   - Contacts are loaded from the `contacts.csv` file.
2. Interactive menu:
   - Users can choose options to add, view, search, or remove contacts.
3. Upon exit:
   - All contact data is saved to the file for future use.

---

## Installation and Setup

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/your-username/contact-book.git
   cd contact-book
