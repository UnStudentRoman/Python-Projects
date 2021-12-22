# Calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calculator(start_number):
    operation = input("+\n-\n*\n/\nPick an operation: ")
    if operation == "+":
        second_number = float(input("What's the next number? : "))
        print(f"{start_number} + {second_number} = {start_number + second_number}")
        return start_number + second_number
    elif operation == "-":
        second_number = float(input("What's the next number? : "))
        print(f"{start_number} - {second_number} = {start_number - second_number}")
        return start_number - second_number
    elif operation == "*":
        second_number = float(input("What's the next number? : "))
        print(f"{start_number} * {second_number} = {start_number * second_number}")
        return start_number * second_number
    elif operation == "/":
        second_number = float(input("What's the next number? : "))
        print(f"{start_number} / {second_number} = {start_number / second_number}")
        return start_number / second_number


print(logo)

start_number = float(input("What's the fist number? : "))
keep_operation = True

while keep_operation == True:
    start_number = calculator(start_number)
    next_move = input(f"Type 'y' to continue calculating with {start_number}, or type 'n' to start a new calculation. If you want to exit type 'x' ")
    if next_move == "x":
        keep_operation = False
    elif next_move == "n":
        start_number = float(input("What's the fist number? : "))