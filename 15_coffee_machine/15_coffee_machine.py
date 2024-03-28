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

def check_price(name):
   
   price = MENU[name]["cost"]
   quarter = int(input("how many quarters?: ")) * 0.25
   dimes = int(input("how many dimes?: ")) * 0.10
   nickles = int(input("how many nickles?: ")) * 0.05
   pennies = int(input("how many pennies?: ")) * 0.01
   # quarter *= 0.25
   # dimes *= 0.10
   # nickles *= 0.05
   # pennies *= 0.01
   all_money = quarter + dimes + nickles + pennies
   if all_money >= price:
      return all_money - price
      # return f"Here is {money - price} in change"
   else:
      return False
      # return f"Sorry that's not enough money. Money refunded."

def check_resources(name):
   ingredients = MENU[name]["ingredients"]
   resources["water"] -= ingredients["water"]
   resources["coffee"] -= ingredients["coffee"]
   if name != "espresso":
      resources["milk"] -= ingredients["milk"]


while True:
   user = input("What would you like? (espresso/latte/cappuccino): ")
   if user == "off":
      break
   if user == "report":
      print(f"Water: {resources['water']}$\nMilk: {resources['milk']}$\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
   # drinks 
   cp = check_price(user)
   if cp == False:
      print(f"Sorry that's not enough money. Money refunded.")
   else:
      print(f"Here is {cp:.2f} in change")
      check_resources(user)

