bars = int(input("Enter the number of sold bars that are not fresh: "))
price = 3.49 
discount = 0.6
cost = bars * price * (1 - discount)
print("The cost of a fresh bar is " + str(price) + "€")
print("The discount on a non-fresh bar is " + str(discount * 100) + "%")
print("The final cost to pay is " + str(round(cost, 2)) + "€")
