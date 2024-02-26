# User Input

# Prompt the user to enter the number of sold, non-fresh bars.
bars = int(input("Enter the number of sold bars that are not fresh: "))

# Define the fixed price per fresh bar.
price = 3.49

# Define the discount percentage for non-fresh bars.
discount = 0.6

# Calculations

# Calculate the total cost 
cost = bars * price * (1 - discount)

# Inform the user of the fresh bar price with the euro symbol (€).
print("The cost of a fresh bar is " + str(price) + "€")

# Inform the user of the discount percentage applied
print("The discount on a non-fresh bar is " + str(discount * 100) + "%")

# Inform the user of the final cost to pay
print("The final cost to pay is " + str(round(cost, 2)) + "€")
