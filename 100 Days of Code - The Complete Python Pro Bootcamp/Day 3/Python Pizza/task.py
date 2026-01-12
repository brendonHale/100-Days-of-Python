print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0

if size == "s" or size == "S":
    total = 15
elif size == "m" or size == "M":
    total = 20
elif size == "l" or size == "L":
    total = 25
else:
    print("Sorry you have to choose either 'S', 'M' or 'L'")

if pepperoni == "y" or pepperoni == "Y":
    if size == "s" or size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "y" or extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}.")
