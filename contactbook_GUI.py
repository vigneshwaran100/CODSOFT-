import tkinter as tk
from tkinter import messagebox, simpledialog

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

    def view_contact_list(self):
        return self.contacts

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

class ContactManagerGUI:
    def __init__(self, root):
        self.contact_manager = Contact()
        self.root = root
        self.root.title("Contact Manager")

        # Add Contact
        self.add_frame = tk.Frame(root)
        self.add_frame.pack(padx=10, pady=10)

        tk.Label(self.add_frame, text="Add Contact").grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(self.add_frame, text="Name:").grid(row=1, column=0, sticky='e')
        self.add_name_entry = tk.Entry(self.add_frame)
        self.add_name_entry.grid(row=1, column=1)

        tk.Label(self.add_frame, text="Phone Number:").grid(row=2, column=0, sticky='e')
        self.add_phone_entry = tk.Entry(self.add_frame)
        self.add_phone_entry.grid(row=2, column=1)

        tk.Label(self.add_frame, text="Email:").grid(row=3, column=0, sticky='e')
        self.add_email_entry = tk.Entry(self.add_frame)
        self.add_email_entry.grid(row=3, column=1)

        tk.Label(self.add_frame, text="Address:").grid(row=4, column=0, sticky='e')
        self.add_address_entry = tk.Entry(self.add_frame)
        self.add_address_entry.grid(row=4, column=1)

        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        # View Contact List
        self.view_button = tk.Button(root, text="View Contact List", command=self.view_contacts)
        self.view_button.pack(pady=5)

        # Search Contact
        self.search_frame = tk.Frame(root)
        self.search_frame.pack(padx=10, pady=10)

        tk.Label(self.search_frame, text="Search Contact").grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(self.search_frame, text="Name or Phone Number:").grid(row=1, column=0, sticky='e')
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(row=1, column=1)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_contact)
        self.search_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Update Contact
        self.update_frame = tk.Frame(root)
        self.update_frame.pack(padx=10, pady=10)

        tk.Label(self.update_frame, text="Update Contact").grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(self.update_frame, text="Name of Contact to Update:").grid(row=1, column=0, sticky='e')
        self.update_name_entry = tk.Entry(self.update_frame)
        self.update_name_entry.grid(row=1, column=1)

        tk.Label(self.update_frame, text="New Name (leave blank to skip):").grid(row=2, column=0, sticky='e')
        self.update_new_name_entry = tk.Entry(self.update_frame)
        self.update_new_name_entry.grid(row=2, column=1)

        tk.Label(self.update_frame, text="New Phone Number (leave blank to skip):").grid(row=3, column=0, sticky='e')
        self.update_new_phone_entry = tk.Entry(self.update_frame)
        self.update_new_phone_entry.grid(row=3, column=1)

        tk.Label(self.update_frame, text="New Email (leave blank to skip):").grid(row=4, column=0, sticky='e')
        self.update_new_email_entry = tk.Entry(self.update_frame)
        self.update_new_email_entry.grid(row=4, column=1)

        tk.Label(self.update_frame, text="New Address (leave blank to skip):").grid(row=5, column=0, sticky='e')
        self.update_new_address_entry = tk.Entry(self.update_frame)
        self.update_new_address_entry.grid(row=5, column=1)

        self.update_button = tk.Button(self.update_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Delete Contact
        self.delete_frame = tk.Frame(root)
        self.delete_frame.pack(padx=10, pady=10)

        tk.Label(self.delete_frame, text="Delete Contact").grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(self.delete_frame, text="Name of Contact to Delete:").grid(row=1, column=0, sticky='e')
        self.delete_name_entry = tk.Entry(self.delete_frame)
        self.delete_name_entry.grid(row=1, column=1)

        self.delete_button = tk.Button(self.delete_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.add_name_entry.get()
        phone_number = self.add_phone_entry.get()
        email = self.add_email_entry.get()
        address = self.add_address_entry.get()
        if name and phone_number and email and address:
            self.contact_manager.add_contact(name, phone_number, email, address)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.add_name_entry.delete(0, tk.END)
            self.add_phone_entry.delete(0, tk.END)
            self.add_email_entry.delete(0, tk.END)
            self.add_address_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def view_contacts(self):
        contacts = self.contact_manager.view_contact_list()
        if contacts:
            contact_list = "\n".join([f"Name: {contact['name']}, Phone: {contact['phone_number']}" for contact in contacts])
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts found!")

    def search_contact(self):
        query = self.search_entry.get()
        results = self.contact_manager.search_contact(query)
        if results:
            result_list = "\n".join([f"Name: {contact['name']}\nPhone Number: {contact['phone_number']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n" for contact in results])
            messagebox.showinfo("Search Results", result_list)
        else:
            messagebox.showinfo("Search Results", "No contacts found!")

    def update_contact(self):
        name = self.update_name_entry.get()
        new_name = self.update_new_name_entry.get() or None
        new_phone_number = self.update_new_phone_entry.get() or None
        new_email = self.update_new_email_entry.get() or None
        new_address = self.update_new_address_entry.get() or None

        updated_contact = self.contact_manager.update_contact(name, new_name, new_phone_number, new_email, new_address)
        if updated_contact:
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Update Error", "Contact not found!")

    def delete_contact(self):
        name = self.delete_name_entry.get()
        if self.contact_manager.delete_contact(name):
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Delete Error", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ContactManagerGUI(root)
    root.mainloop()
