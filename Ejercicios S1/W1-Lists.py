nameList = ["Pedro", "Juan", "Pedrito","Juanito","Juanon", "Pedrón"]
hourList = [40, 50, 20, 23, 30, 42]
priceList = [35, 12, 22, 11, 14, 100]

i = 0
while i < 6:
    print("The worker " + nameList[i] + " who worked " + str(hourList[i]) + " hours with an hourly cost of: $" + str(priceList[i]))
    i += 1
