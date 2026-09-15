import json
import os

FILE_NAME = "contacts.json"


# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("Contact added successfully!")


# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List")
    print("-" * 40)

    for name, details in contacts.items():
        print("Name:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
        print("-" * 40)


# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email

        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# Main program
contacts = load_contacts()

while True:
    print("\n" + "=" * 40)
    print("       CONTACT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        edit_contact(contacts)

    elif choice == "4":
        delete_contact(contacts)

    elif choice == "5":
        print("Thank you for using Contact Management System!")
        break

    else:
        print("Invalid choice. Please try again.")