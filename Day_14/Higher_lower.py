import art
from data import data
import random

print(art.logo)

player_score = 0
game_over = False
guess_a = random.choice(data)

def compare(A,B):
    player_guess = input("Who has more followers? Type 'A' or 'B':").upper()
    if A["follower_count"] > B["follower_count"]:
        answer = "A"
    else:
        answer = "B"
    if player_guess == answer:
        return 1
    else:
        return 0

while game_over == False:
    guess_b = random.choice(data)
    while guess_a["name"] == guess_b["name"]:
        guess_b = random.choice(data)
    print(f"Compare A: {guess_a['name']}, a {guess_a['description']}, from {guess_a['country']}.")
    print(art.vs)
    print(f"Against B: {guess_b['name']}, a {guess_b['description']}, from {guess_b['country']}.")
    if compare(A=guess_a, B=guess_b) == 0:
        game_over = True
        print(f"Wrong. You lose. Your score is {player_score}.\n")
    else:
        player_score += 1
        print(f"Correct. Your score is {player_score}.\n")
        guess_a = guess_b