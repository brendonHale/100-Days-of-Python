rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

compChoice = random.randint(0,2)
print("Computer chose:")
if compChoice == 0:
    print(rock)
elif compChoice == 1:
    print(paper)
else:
    print(scissors)

if (choice == 0 and compChoice == 1) or (choice == 1 and compChoice == 2) or (choice == 2 and compChoice == 0):
    print("You Lose")
elif (choice == compChoice):
    print("Draw")
else:
    print("You Win")