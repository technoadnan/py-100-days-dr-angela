import calc_art as art

print(art.logo)

def add(n1, n2):
   return n1 + n2
def sub(n1, n2):
   return n1 - n2
def mult(n1, n2):
   return n1 * n2
def div(n1, n2):
   return n1 / n2


operations = {
   "+" : add,
   "-" : sub,
   "*" : mult,
   "/" : div
}

num1 = int(input("What's the first number?: "))
for j in operations:
   print(j)

def calc():
   while True:
      operation_symbol = input("Pick an operation from the line above: ")
      num2 = int(input("What's the next number?: "))

      if operation_symbol in operations:
         answer = operations[operation_symbol](num1,num2) # the reason we can access 'answer' b/c after we call the func() its returing something 

      print(f"{num1} {operation_symbol} {num2} = {answer}")

      bool_yes_no = input("Type 'y' to continue calculating with 8, or type 'n' to exit.: ")
      if bool_yes_no == "y":
         num1 = answer
         continue
      else:
         calc()
         break
calc()