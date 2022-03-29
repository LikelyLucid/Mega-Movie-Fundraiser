name = ""
count = 0
MAX_TICKETS = 5  # max amount of tickets

while name != "Xxx" and count != MAX_TICKETS:
    if MAX_TICKETS - count > 1:  # if there are more than 1 tickets left
        print(f"\nYou have {MAX_TICKETS - count} ticket left")
    else:
        # if there is only 1 ticket left
        print("\n****YOU ONLY HAVE ONE TICKET LEFT*****")
    name = input("What's your name? ").title()
    if name != "Xxx":
        count += 1

if count < MAX_TICKETS:
    print(
        f"\nYou have sold {count} tickets\nThere are {MAX_TICKETS - count} tickets left"
    )
else:
    print("\nYou have sold all available tickets")
