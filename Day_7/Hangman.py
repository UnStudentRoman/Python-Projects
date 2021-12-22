#Hangman

import random
import hangman_stages
import hangman_word_list


hidden_word = []
chosen_word = random.choice(hangman_word_list.word_list)

print(hangman_stages.logo)

for letter in chosen_word:
    hidden_word.append("_")
print(' '.join(hidden_word))
#print(hidden_word)

lives = 0

while hidden_word.count("_") > 0 and lives < 6:
    print(hangman_stages.hangman_stages[lives])
    guess_letter = input("Guess a letter of the word. ").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess_letter:
            #print(position)
            hidden_word.insert(position,guess_letter)
            hidden_word.pop(position+1)
    if not chosen_word.count(guess_letter) > 0:
        lives += 1
    print(' '.join(hidden_word))

if hidden_word.count("_") > 0:
    print(hangman_stages.hangman_stages[lives])
    print("You lost. The word was", chosen_word)
else:
    print("You won!")