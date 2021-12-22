
import random

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

rock_paper_scissors = [rock,paper,scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
calculator_choice = random.randint(0,2)

print(calculator_choice)

if player_choice == 0 and calculator_choice == 2:
    print("You win!")
elif player_choice == 2 and calculator_choice == 0:
    print("You lose!")
elif player_choice < calculator_choice:
    print("Computer wins!")
elif player_choice == calculator_choice:
    print("It's a draw!")
elif player_choice > 2:
    print("Invalid choice. You lose")
elif player_choice > calculator_choice:
    print("You win!")



print("You played ", rock_paper_scissors[player_choice])
print("Computer played ", rock_paper_scissors[calculator_choice])

k = input("press close to exit")