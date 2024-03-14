print("Welcome to secret auction program")
bidders_info = {}
highest_bid = 0
name_bidder = ""
while True:
   name = input("What is your name?: ")
   bid = input("What's your bid?: ")
   boolean_bid = input("Are there any other bidders? Type 'yes' or 'no': ")
   bidders_info[name] = bid
   if boolean_bid == "no":
      break

for name in bidders_info:
   if int(bidders_info[name]) > highest_bid:
      highest_bid = int(bidders_info[name])
      name_bidder = name

print(f"The winner is {name_bidder} with a bid of ${highest_bid}")

