from menu import MENU
from menu import resources

def check_resources(drink):
    if drink == "espresso":
        if MENU[drink]['ingredients'].get("water") > resources.get("water"):
            print("Not enough water.")
        elif MENU[drink]['ingredients'].get("coffee") > resources.get("coffee"):
            print("Not enough coffee.")
        else:
            coin_calculator(drink)
    elif drink == "latte" or drink == "cappuccino":
        if MENU[drink]['ingredients'].get("water") > resources.get("water"):
            print("Not enough water.")
        elif MENU[drink]['ingredients'].get("coffee") > resources.get("coffee"):
            print("Not enough coffee.")
        elif MENU[drink]['ingredients'].get("milk") > resources.get("milk"):
            print("Not enough milk.")
        else:
            coin_calculator(drink)
    else:
        print(report())

def consume_resources(drink):
    if drink == "espresso":
        resources["water"] -= MENU[drink]['ingredients'].get("water")
        resources["coffee"] -= MENU[drink]['ingredients'].get("coffee")
    else:
        resources["water"] -= MENU[drink]['ingredients'].get("water")
        resources["coffee"] -= MENU[drink]['ingredients'].get("coffee")
        resources["milk"] -= MENU[drink]['ingredients'].get("milk")
    print(f"Enjoy your {drink}.")

def coins_inserted():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))*0.25
    dimes = int(input("How many dimes? "))*0.1
    nickles = int(input("How many nickles? "))*0.05
    pennies = int(input("How many pennies? "))*0.01
    return quarters + dimes + nickles + pennies

def coin_calculator(drink):
    user_money = coins_inserted()
    if user_money > MENU[drink]["cost"]:
        resources["money"] += MENU[drink]["cost"]
        consume_resources(drink)
        print(f"Here is $ {user_money - MENU[drink]['cost']} in change.")
    elif user_money == MENU[drink]["cost"]:
        resources["money"] += MENU[drink]["cost"]
        consume_resources(drink)
    else:
        print("Sorry that's not enough money. Money refunded.")

def report():
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    money = resources["money"]
    return f"Resources report:\nWater: {water}ml\nCoffee: {coffee}g\nMilk: {milk}ml\nMoney: ${money}"

coffee_machine_on = True

while coffee_machine_on:
    user_drink = input("What would you like? (Espresso - $1.50/Latte - $2.50/Cappuccino - $3): ").lower()
    if user_drink == "off":
        coffee_machine_on = False
        break
    check_resources(user_drink)