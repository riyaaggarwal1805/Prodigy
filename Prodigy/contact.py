import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    if name in contacts:
        print("A contact with this name already exists.")
        return
    
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")

    if name not in contacts:
        print("Contact not found.")
        return
    
    print("Leave the field empty if you do not want to change it.")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
    email = input(f"Enter new email address (current: {contacts[name]['email']}): ")
    
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    
    save_contacts(contacts)
    print(f"Contact {name} updated successfully.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")

    if name not in contacts:
        print("Contact not found.")
        return
    
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact {name} deleted successfully.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
