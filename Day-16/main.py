# class HumanInformation:
#     name = ""
#     surname = ""
#     age = 0
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info(self):
#         print(f"I'm {self.name} {self.surname}")
#         print(f"My age is {self.age}")
#
#
# akin = HumanInformation("Akin", "Aykut", 25)
#
# akin.info()

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine:
    def __init__(self):
        """Define other class to make coffee"""
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.menu = Menu()
        print("Coffee Machine activated.")

    def run(self):
        """Main method which one is running when coffee machine is running."""
        while True:
            data = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if data == "latte":
                self.make_coffee(data)
            elif data == "espresso":
                self.make_coffee(data)
            elif data == "cappuccino":
                self.make_coffee(data)
            elif data == "report":
                self.report()
            elif data == "off":
                print("Coffee Machine is closing...")
                break
            else:
                print("You entered wrong request.")
                break

    def report(self):
        """To get information about coffee machine"""
        self.coffee_maker.report()
        self.money_machine.report()

    def make_coffee(self, coffee_name):
        """To make coffee using other class"""
        drink = self.menu.find_drink(coffee_name)
        if self.coffee_maker.is_resource_sufficient(drink) and self.money_machine.make_payment(drink.cost):
            self.coffee_maker.make_coffee(drink)


machine = CoffeeMachine()
machine.run()
