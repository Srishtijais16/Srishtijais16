contacts = []
def add_contact():
    contacts.append({
        'name': input("Enter Name: "),
        'phone_number': input("Enter Phone Number: "),
        'email': input("Enter Email Address: ")
    })
    print("Contact added successfully!")
def display_contacts():
    if contacts:
        print("\tName\t\tPhone Number\t\tEmail")
        for contact in contacts:
            print(f'\t{contact["name"]}\t\t{contact["phone_number"]}\t\t{contact["email"]}')
    else:
        print("No contacts found.")
def search_contact():
    search_name = input("Enter the Name to search: ").lower()
    for contact in contacts:
        if contact['name'].lower() == search_name:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}")
            return
    print(f"Contact with name '{search_name}' not found.")
def delete_contact():
    delete_name = input("Enter the Name to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == delete_name:
            contacts.remove(contact)
            print(f"Contact '{delete_name}' deleted successfully.")
            return
    print(f"Contact with name '{delete_name}' not found.")
while True:
    print("\nContact Book Menu:")
    print("1. Add New Contact")
    print("2. Display All Contacts")
    print("3. Search for a Contact")
    print("4. Delete a Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
