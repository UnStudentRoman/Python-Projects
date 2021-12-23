############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

#################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import art_file
import random

def draw_card():
    return random.choice(cards)

def get_score(hand):
    player_score = 0
    player_score = sum(hand)
    if player_score > 21 and hand.count(11) != 0:
        player_score += hand.count(11)*10
    return player_score

print(art_file.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play_game == "y":

    player_cards = []
    dealer_cards = []
    #Draw starting cards
    for i in range(0,2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())

    player_score = get_score(player_cards)
    dealer_score = get_score(dealer_cards)

    if dealer_score < 17:
        dealer_cards.append(draw_card())

    print(f"Your hand is {player_cards}, total score is {player_score}")
    print(f"Dealer's hand is {dealer_cards[0]}, dealer's score is {dealer_cards[0]}.")


    draw_another = input("Type 'y' to draw another card. Type 'n' to pass. ")

    while draw_another == "y":
        player_cards.append(draw_card())
        player_score = get_score(player_cards)
        if player_score > 21:
            break
        print(f"Your hand is {player_cards}, total score is {player_score}")
        draw_another = input("Type 'y' to draw another card. Type 'n' to pass. ")
        if draw_another == "n":
            break


    #Winning conditions
    if player_score > 21:
        print(f"Your hand is {player_cards}, total score is {player_score}. You've gone bust! You lose.")

    if player_score <= 21 and player_score > dealer_score:
        print(f"Your hand is {player_cards}, total score is {player_score}\nDealer's hand is {dealer_cards}, dealer's score is {dealer_score}.\n\n You win!")

    if player_score <= 21 and player_score < dealer_score:
        print(f"Your hand is {player_cards}, total score is {player_score}\nDealer's hand is {dealer_cards}, dealer's score is {dealer_score}.\n\n You lose!")

    if player_score <= 21 and player_score == dealer_score:
        print(f"Your hand is {player_cards}, total score is {player_score}\nDealer's hand is {dealer_cards}, dealer's score is {dealer_score}.\n\n It's a draw!")
    play_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")