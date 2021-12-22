#Prime Number Checker
import math

number_check = int(input("What number do you want to check? "))
max_to_check = math.sqrt(number_check)

def prime_checker(number):
    is_prime = True
    for i in range(2,int(max_to_check)+1):
        if number%i == 0:
            is_prime = False
    if is_prime == False:
        print(f"The number {number_check} is not a prime.")
    else:
        print(f"The number {number_check} is a prime.")

prime_checker(number_check)