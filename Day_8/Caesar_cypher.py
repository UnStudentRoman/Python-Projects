#Caesar cypher

import string
letters = list(string.ascii_lowercase)
finish = False

def caesar(text, shift, direction):
    encrypt_text = []
    if direction == "encode":
        for letter in text:
            if letters.count(letter) == 0:
                encrypt_text.append(letter)
            else:
                position = letters.index(letter) + shift
                if position >= len(letters):
                    position = position - len(letters)
                encrypt_text.append(letters[position])
            # print(letter, position)
        print("Your message is encoded now!", "".join(encrypt_text))
    elif direction == "decode":
        for letter in text:
            if letters.count(letter) == 0:
                encrypt_text.append(letter)
            else:
                position = letters.index(letter) - shift
                encrypt_text.append(letters[position])
            # print(letter, position)
        print("Your message is decoded now!", "".join(encrypt_text))

while finish == False:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt.\n")
    text = input("Type your message here: \n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    caesar(text, shift, direction)
    repeat = input("Type 'yes' to decrypt or encrypt another message or type 'no' to exit.\n")
    if repeat == "no":
        finish = True
print("Goodbye!")