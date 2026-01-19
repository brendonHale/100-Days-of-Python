# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
print("Welcome to the secret auction program.")

auctions = { }

bidding = True

while bidding:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    auctions[name] = bid

    next = input("Are there any other bidders? Type 'y' or 'n': ")
    if next == "n":
        highest_bid = 0
        winner = ""
        bidding = False

        for key in auctions:
            bid = auctions[key]
            if bid > highest_bid:
                highest_bid = bid
                winner = key

        print(f"The winner is {winner} with a bid of {highest_bid}.")
