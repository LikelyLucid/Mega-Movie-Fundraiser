name = ""
count = 0
MAX_TICKETS = 5  # max amount of tickets

while name != "Xxx" and count != MAX_TICKETS:  # while loop
    print(f"You have {MAX_TICKETS - count} tickets left")
    name = input("What's your name? ").title()
    count += 1

if count < MAX_TICKETS:
    print(f"You have sold {count} tickets\nThere are {MAX_TICKETS - count} tickets left")
else:
    print("You have sold all available tickets")