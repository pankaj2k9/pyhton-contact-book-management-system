import csv

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def save_contacts(self, contacts):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Phone", "Name", "Email", "Address"])
            for phone, details in contacts.items():
                writer.writerow([phone, details['name'], details['email'], details['address']])

    def load_contacts(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                return {row["Phone"]: {"name": row["Name"], "email": row["Email"], "address": row["Address"]} for row in reader}
        except FileNotFoundError:
            return {}
