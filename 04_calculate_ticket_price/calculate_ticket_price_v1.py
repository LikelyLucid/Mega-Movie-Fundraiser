def calculate_ticket_price(age):
    CHILD_AGE = range(12, 16)
    STANDARD_AGE = range(16, 65)

    STANDARD_PRICE = 10.5
    if age in CHILD_AGE:
        return 7.5
    elif age in STANDARD_AGE:
        return STANDARD_PRICE
    else:
        return 6.5


name = input("Name: ")
age = int(input("Age: "))
print(f"The price is ${calculate_ticket_price(age):,.2f}")