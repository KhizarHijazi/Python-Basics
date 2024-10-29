"""Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday."""

age = int(input("Enter Your age :"))
day_input = input("what day is today? enter here :").lower()
adult_price = 12
child_price = 8
if age < 18 :
    price = child_price
else :
    price = adult_price
if day_input == "wednesday" :
    price -= 2

if age < 18 :
    print("Ticket price for children:", price, "$")
else:
    print("Ticket price for adults:", price, "$")

