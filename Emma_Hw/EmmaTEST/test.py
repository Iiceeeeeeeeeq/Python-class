ticket_adult = int(input("How many adult tickets do you have? : "))
ticket_child = int(input("How many children tickets do you have? : "))
member = input("Are you a member of our museum? \
fill in with \"T\" if you are \"F\" if you aren't : ").upper()

price_adult = ticket_adult*100
price_child = ticket_child*50
all_price = price_adult + price_child
all_ticket = ticket_adult + ticket_child

if member == "T":
    if ticket_child == 0:
        total_price = all_price * 0.9
    elif all_ticket >= 10:
        total_price = all_price * 0.5
    elif all_ticket >= 5:
        total_price = all_price * 0.7
    elif all_ticket < 5:
        total_price = all_price * 0.8

elif member == "F":
    total_price = all_price * 0.95

else:
    raise KeyError("Error")

print (f"Total price is {total_price} Baht")