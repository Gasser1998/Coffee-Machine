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
    }
money = 0


def check_resources(user_choice):
    global resources
    if user_choice != 'espresso':
        if resources["water"] - MENU[user_choice]["ingredients"]["water"] < 0:
            return "water"
        elif resources["milk"] - MENU[user_choice]["ingredients"]["milk"] < 0:
            return "milk"
        elif resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"] < 0:
            return "coffee"
        else:
            resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
            resources["water"] -= MENU[user_choice]["ingredients"]["water"]
            return "enough"
    else:
        if resources["water"] - MENU[user_choice]["ingredients"]["water"] < 0:
            return "water"
        elif resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"] < 0:
            return "coffee"
        else:
            resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            resources["water"] -= MENU[user_choice]["ingredients"]["water"]
            return "enough"


def change_calculator(quarters, dimes, nickels, pennies, user_choice):
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.10
    total_nickels = nickels * 0.05
    total_pennies = pennies * 0.01
    total_amount = total_quarters + total_dimes + total_nickels + total_pennies
    order_total = MENU[user_choice]["cost"]
    if total_amount >= order_total:
        return round(total_amount - order_total, 2)
    else:
        return "no go"


def coffee_machine():
    global resources
    global money
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee:{resources['coffee']}g")
        print(f"Money: ${money}")
        coffee_machine()
    elif order == "refill":
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        money = 0
        print("Machine has been refilled and the money has been withdrawn.")
        coffee_machine()
    elif order == "off":
        print("Turning off coffee machine, goodbye.")
        exit()
    if check_resources(order) != "enough":
        print(f"Sorry there is not enough {check_resources(order)}.")
        coffee_machine()
    else:
        check_resources(order)
        print("Please insert coins")
        quarters = int(input("Please insert quarters: "))
        dimes = int(input("Please insert dimes: "))
        nickels = int(input("Please insert nickels: "))
        pennies = int(input("Please insert pennies: "))
        if change_calculator(quarters, dimes, nickels, pennies, order) != "no go":
            money += MENU[order]["cost"]
            print(f"Here is ${change_calculator(quarters, dimes, nickels, pennies, order)} in change.")
            print(f"Here is your {order} ☕. Enjoy! :)")
            coffee_machine()
        else:
            print("That is not enough money. Money refunded")
            coffee_machine()


coffee_machine()
