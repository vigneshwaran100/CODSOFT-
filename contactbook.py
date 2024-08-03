class Contact:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        return self.contacts

    def view_contact_list(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone_number']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if contact["name"].lower() == query.lower() or contact["phone_number"] == query]
        return results

    def update_contact(self, name, new_name=None, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                if new_name:
                    contact["name"] = new_name
                if new_phone_number:
                    contact["phone_number"] = new_phone_number
                if new_email:
                    contact["email"] = new_email
                if new_address:
                    contact["address"] = new_address
                return contact
        return None

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                return True
        return False


def main():
    contact_manager = Contact()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)
            print("Contact added successfully!")

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                for contact in results:
                    print(f"Name: {contact['name']}")
                    print(f"Phone Number: {contact['phone_number']}")
                    print(f"Email: {contact['email']}")
                    print(f"Address: {contact['address']}")
            else:
                print("No contacts found!")

        elif choice == "4":
            name = input("Enter name of contact to update: ")
            new_name = input("Enter new name (press enter to skip): ")
            new_phone_number = input("Enter new phone number (press enter to skip): ")
            new_email = input("Enter new email (press enter to skip): ")
            new_address = input("Enter new address (press enter to skip): ")
            updated_contact = contact_manager.update_contact(name, new_name or None, new_phone_number or None, new_email or None, new_address or None)
            if updated_contact:
                print("Contact updated successfully!")
            else:
                print("Contact not found!")

        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            if contact_manager.delete_contact(name):
                print("Contact deleted successfully!")
            else:
                print("Contact not found!")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()