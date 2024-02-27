class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(f"\nName: {contact.name}, \nPhone: {contact.phone_number}, \nEmail: {contact.email}, \nAddress: {contact.address}")
        else:
            print("No contacts to display.")

    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"\nName: {contact.name}, \nPhone: {contact.phone_number}, \nEmail: {contact.email}, \nAddress: {contact.address}")
                found = True
                break
        if not found:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n*** Contact Book Menu ***")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter store_name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            name = input("Enter store_name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
