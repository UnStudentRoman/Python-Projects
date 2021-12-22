#Password Generator

import string
import random
password = []
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

password_length = int(input("How long do you want your password to be? "))
numbers_number = int(input("How many numbers would you like in your password? "))
symbol_number = int(input("How many symbols would you like in your password? "))

for letter in range(1, password_length+1 - numbers_number - symbol_number):
    password.append(random.choice(letters))
for letter in range(1, numbers_number+1):
    password.append(random.choice(numbers))
for letter in range(1, symbol_number+1):
    password.append(random.choice(symbols))

random.shuffle(password)
print("Your password is :", ''.join(password))