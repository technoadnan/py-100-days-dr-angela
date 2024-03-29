from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money = MoneyMachine()
men = Menu()

while True:
   user = input(f"{men.get_items()}: ")
   if user == "off":
      break
   elif user == "report":
      coffee_maker.report()
      money.report()
   else:
      drink = men.find_drink(user)
      if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

