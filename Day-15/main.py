# Coffee Machine App

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(coffee):
    count = 0
    water = MENU[coffee]["ingredients"]["water"]
    coffee1 = MENU[coffee]["ingredients"]["coffee"]

    if coffee != "espresso":
        milk = MENU[coffee]["ingredients"]["milk"]
        if resources["milk"] - milk > 0:
            count += 1
        else:
            print("Sorry there is not enough milk.")
    if resources["water"] - water > 0:
        count += 1
    else:
        print("Sorry there is not enough water.")
    if resources["coffee"] - coffee1 > 0:
        count += 1
    else:
        print("Sorry there is not enough coffee.")

    if coffee == "expresso" and count == 2:
        return True
    elif count == 3:
        return True
    else:
        return False


def calculate_user_money(quarter, dimes, nickles, pennies):
    total_money = (quarter * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total_money


def get_user_money():
    print("Please insert coins.")
    quarter = float(input("How many quarter?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("How many pennies?"))
    the_money = calculate_user_money(quarter, dimes, nickles, pennies)
    return the_money


def add_money(coffee_type):
    money = MENU[coffee_type]["cost"]
    resources["money"] += money


def check_money(money, coffee_type):
    if money < MENU[coffee_type]["cost"]:
        return False
    else:
        return True


def check_input(data):
    if data == "espresso":
        return True
    elif data == "latte":
        return True
    elif data == "cappuccino":
        return True
    else:
        return False


while True:

    type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if check_input(type_of_coffee) and check_resources(type_of_coffee):
        user_money = get_user_money()
        if check_money(user_money, type_of_coffee):
            add_money(type_of_coffee)
            user_money -= MENU[type_of_coffee]["cost"]
            resources["water"] -= MENU[type_of_coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[type_of_coffee]["ingredients"]["coffee"]
            if type_of_coffee != "espresso":
                resources["milk"] -= MENU[type_of_coffee]["ingredients"]["milk"]

            print(f"Here is ${round(user_money, 2)} dollars in change.")
            print("Here is your latte enjoy!")

        else:
            print("Sorry that's not enough money. Money refunded.")
    elif type_of_coffee == "report":
        report()
    elif type_of_coffee == "off":
        print("Machine is closing...")
        break
    else:
        print("You did anything...")

