name = ""
count = 0
MAX_TICKETS = 5  # max amount of tickets

while name != "Xxx" and count != MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"You have {MAX_TICKETS - count} ticket left")
    else:
        print("****YOU ONLY HAVE ONE TICKET LEFT*****")
    name = input("What's your name? ").title()
    count += 1

if count < MAX_TICKETS:
    print(f"You have sold {count} tickets\nThere are {MAX_TICKETS - count} tickets left")
else:
    print("You have sold all available tickets")