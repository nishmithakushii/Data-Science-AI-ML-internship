contacts = {
    "Asha": "9876543210",
    "Ravi": "9123456789",
    "Meena": "9988776655"
}
contacts["Kiran"] = "9012345678"
contacts["Ravi"] = "9000000000"
print(contacts.get("Asha", "Contact not found"))
print(contacts.get("Rahul", "Contact not found"))
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
