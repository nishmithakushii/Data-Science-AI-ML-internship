contact_book={"alice":"123-456-7890",
              "bob":"987-654-3210","cary":"555-555-5555"}
print(contact_book)
contact_book["judy"]="111-111-1111"
print(contact_book)
new_contact={"dave":"222-222-2222"}
contact_book.update(new_contact)
print(contact_book)