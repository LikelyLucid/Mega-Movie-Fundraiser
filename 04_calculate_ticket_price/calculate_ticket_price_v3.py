def calculate_ticket_price(age):
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in CHILD_AGE:
        ticket_price = CHILD_PRICE
    elif age in STANDARD_AGE:
        ticket_price = STANDARD_PRICE
    else:
        ticket_price = RETIRED_PRICE
    return ticket_price


test_cases = [["Rangi", 15], ["Manaia", 16], ["Talia", 64], ["Arihi", 65]]

for test in test_cases:
    test_name = test[0]
    test_age = test[1]
    print(f"For {test_name} the price is ${calculate_ticket_price(test_age):,.2f}")
