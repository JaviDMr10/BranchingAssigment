# Branching assigment

#rates in cents:
RATE_FIRST_1000 = 7.633
RATE_ABOVE_1000 = 9.259

#Enter the user inputs: 1500, 764, 1215, and 812.
userInput = input("Enter the KW hours used: ")

kw_hours = float(userInput)

# Condition: if it is less than 1000 hours and more than that:
if kw_hours <= 1000:
    total = (RATE_FIRST_1000 / 100) * kw_hours
else:
    price1 = (RATE_FIRST_1000 / 100) * 1000
    price2 = (RATE_ABOVE_1000 / 100) * (kw_hours - 1000)
    total = price1 + price2

print("The amount owed is: $%.2f" % total)






