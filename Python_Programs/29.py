contacts = {
    "raj": "9876543210",
    "shubham": "9123456780",
    "sahil": "9988776655"
}

name = input("Enter the contact name to search: ")

if name in contacts:
    print(f"{name.title()}'s contact number is {contacts[name]}")
else:
    print("Contact not found")