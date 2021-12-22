#Rock, paper, scissors

import random

player = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors."))

calculator = [1, 2, 3]
calculator_pick = random.choice(calculator)

if player == 1 and calculator_pick == 1:
    print("You both chose rock. It's a draw.")
elif player == 2 and calculator_pick == 1:
    print("Paper covers rock. You win!")
elif player == 3 and calculator_pick == 1:
    print("Rock curshes scissors. You lose!")
elif player == 1 and calculator_pick == 2:
    print("Paper covers rock. You lose!")
elif player == 2 and calculator_pick == 2:
    print("You both chose paper. It's a draw.")
elif player == 3 and calculator_pick == 2:
    print("Scissors cuts paper. You win!")
elif player == 1 and calculator_pick == 3:
    print("Rock curshes scissors. You win!")
elif player == 2 and calculator_pick == 3:
    print("Scissors cuts paper. You lose!")
else:
    print("You both chose scissors. It's a draw.")