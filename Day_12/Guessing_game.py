#Guessing game

import random

print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")
lives = 5
if difficulty == "easy":
    lives = 10

answer = random.randint(0,100)
game_end = False
player_guess = int(input("Make a guess: "))

while lives > 0 and game_end == False:
    if player_guess > answer:
        lives -= 1
        print(f"Too high!\nGuess again.\nYou have {lives} attempts remaining to guess the number.")
    elif player_guess < answer:
        lives -= 1
        print(f"Too low!\nGuess again.\nYou have {lives} attempts remaining to guess the number.")
    else:
        game_end = True
        print("You guessed right")
        break
    player_guess = int(input("Try again: "))