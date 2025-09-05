from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


for item in menu.menu:
    print(f"{item.name.title()}: ${item.cost}")
order_name = input("What would you like to purchase?").lower()

drink = menu.find_drink(order_name)

if drink and coffee_maker.is_resource_sufficient(drink):
    if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
