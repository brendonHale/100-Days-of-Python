from random import randint
from art import logo

EASY = 10
HARD = 5

def check_guess(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You Win! The number was {answer}")

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY
    else:
        return HARD

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")

    turns = difficulty()

    guess = -1

    while guess != answer:
        print(f"You have {turns} guesses left")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print(f"You lose! The number was {answer}")
        elif guess != answer:
            print("Guess again.")

game()