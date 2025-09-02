from copyreg import constructor


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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01


def check_water_resource(water):
    if MENU[coffee_of_choice]["ingredients"]["water"] >= resources["water"]:
        print(f"Machine too low on water for an {coffee_of_choice}")
        return False
    else:
        return True


def check_milk_resource(milk):
    if "milk" not in MENU[coffee_of_choice]["ingredients"]:
        return True
    if MENU[coffee_of_choice]["ingredients"]["milk"] >= resources["milk"]:
        print(f"Machine too low on milk for an {coffee_of_choice}")
        return False
    else:
        return True


def check_coffee_resource(coffee):
    if MENU[coffee_of_choice]["ingredients"]["coffee"] >= resources["coffee"]:
        print(f"Machine too low on coffee for an {coffee_of_choice}")
        return False
    else:
        return True


def accept_coins(quarter, dime, nickel, penny):
    global profit
    payment = 0
    print(f"The price is {MENU[coffee_of_choice]['cost']}")
    quarters = int(input("How many quarters? "))
    for _ in range(0, quarters):
        profit += quarter
        payment += quarter
    dimes = int(input("How many dimes? "))
    for _ in range(0, dimes):
        profit += dime
        payment += dime
    nickels = int(input("How many nickels? "))
    for _ in range(0, nickels):
        profit += nickel
        payment += nickel
    pennies = int(input("How many pennies? "))
    for _ in range(0, pennies):
        profit += penny
        payment += penny

    """ check if they paid enough """
    if payment == MENU[coffee_of_choice]["cost"]:
        print(f"Here's your {coffee_of_choice}")
    elif payment >= MENU[coffee_of_choice]["cost"]:
        print(f"Here is your change {abs(MENU[coffee_of_choice]['cost'] - payment)}")
        print(f"Here's your {coffee_of_choice}")
    elif payment <= MENU[coffee_of_choice]["cost"]:
        print(
            f"You are short {abs(payment - MENU[coffee_of_choice]['cost'])}, but here's one on the house."
        )
    print(f"Your payment: {payment}")


valid_choices = MENU.keys()  # ['espresso', 'latte', 'cappuccino']


def main_loop():
    global coffee_of_choice
    using = True
    while using:
        coffee_of_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_of_choice == "off":
            print("Turning off")
            using = False
        elif coffee_of_choice == "report":
            print(f"${profit}")
        elif coffee_of_choice in valid_choices:
            water_ok = check_water_resource(resources["water"])
            milk_ok = check_milk_resource(resources["milk"])
            coffe_ok = check_coffee_resource(resources["coffee"])

            if water_ok and milk_ok and coffe_ok:
                accept_coins(quarter, dime, nickel, penny)

        else:
            print("Not a valid coffee. Choose espresso, latte, or cappuccino.")


main_loop()
