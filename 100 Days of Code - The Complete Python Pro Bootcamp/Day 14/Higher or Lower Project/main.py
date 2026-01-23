from art import logo, vs
from game_data import data
import random


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game = True
account_b = random.choice(data)

while game:
    account_a = account_b
    account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_count = account_a["follower_count"]
    b_count = account_b["follower_count"]

    answer = check_answer(guess, a_count, b_count)

    if answer:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Incorrect. Final score: {score}")
        game = False
