import random

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

pictures = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("\nYour chose:\n" + pictures[player_choice] + "\n")

computer_choice = random.randint(0, 2)
print("Computer chose:\n" + pictures[computer_choice] + "\n")

if player_choice == 0:
  if computer_choice == 1:
    print("You lose.")
  elif computer_choice == 2:
    print("You won.")
  else:
    print("It's a draw.")

elif player_choice == 1:
  if computer_choice == 2:
    print("You lose.")
  elif computer_choice == 0:
    print("You won.")
  else:
    print("It's a draw.")

elif player_choice == 2:
  if computer_choice == 0:
    print("You lose.")
  elif computer_choice == 1:
    print("You won.")
  else:
    print("It's a draw.")