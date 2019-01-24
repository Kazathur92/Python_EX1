stockDict = { "PB": "Peanut Butter",
"JJ": "Jelly Jam", "CM": "Chicken Monkey"}

purchases = [ ("PB", 300, "09-jan-2019", 15),
 ("JJ", 200, "08-jan-2019", 20),
 ("CM", 600, "10-dec-2018", 10) ]

report = {}

# this as is just selects the key
for fullName in stockDict:
  # below you do stockDict[fullName] to target the value inside the key
  print("{0}".format(stockDict[fullName]))
  for stock in purchases:
    print("full stock", stock)
    # this is matching full name which is the key to the first item in stock
    # to get the individual item inside stock use square brackets and the index ex: stock[1] to target the stock number
    if fullName == stock[0]:
      calculation = stock[1] * stock[3]
      print("{0}".format(stock))
      print(calculation, stockDict[fullName])
      # the way to do template literal here is to grab the number of the argument and stick it in where you want it in the string
      print("I purchased {0} stock for {1}".format(stockDict[fullName], calculation))


# The broccoli way
# for purchase in purchases:
#   abbrev = purchase[0]
#   full_Name = stockDict[abbrev]
#   no_of_shares = purchase[1]
#   purch_date = purchase[2]
#   purch_price = purchase[3]
#   full_purchase_price = no_of_shares * purch_price
#   print(f"I purchased {full_Name} stock on {purch_date} for ${full_purchase_price}")

#   try:
#     report[abbrev].append(purchase)
#   except KeyError:
#     report[abbrev] = list()
#     report[abbrev].append(purchase)

# for abbrev, purchases in report.items():
#   print(f"-------{abbrev}--------")
#   total_portfolio_stock_value = 0
#   for purchase in purchases:
#     total_portfolio_stock_value += purchase[1] * purchase[3]
#     print(f"     {purchase}")
#     print(f"Total value of stock in portfolio: ${total_portfolio_stock_value}\n\n")


    # Comprehensions
flowers = ["lily", "shapdragon", "rose"]
bees = ["bumblebee", "honeybee", "dobee"]

# way #1
# flowers_quotes = []
# for flower in flowers:
#   flowers_quotes.append(f"{flower}s make me sneeze")

# print(flowers_quotes)

# way #2
flowers_quotes = [f"{flower}s make me sneeze" for flower in flowers]

# print(flowers_quotes)

# way #1
# large_flowers = []
# for flower in flowers:
#   for bee in bees:
#     large_flowers.append(f"the {bee} pollinates the {flower}.")

# print(large_flowers)

# way #2
# large_flowers = [f"the {bee} pollinates the {flower}."
# for flower in flowers
# for bee in bees]

# print(large_flowers)