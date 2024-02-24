print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size you want for your pizza? ")
bill = 0
if size == 'S':
    bill += 15

elif size == 'M':
    bill += 20

else:
    bill += 25

add_pepperoni = input("Do you want to add pepperoni: Y or N ")
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

add_cheese = input("Do you want to add cheese: Y or N")
if add_cheese == "Y":
    bill += 1


print(f'Your final bill is {bill}')
