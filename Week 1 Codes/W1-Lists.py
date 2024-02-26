# Workers
nameList = ["Pedro", "Juan", "Pedrito", "Juanito", "Juanon", "Pedrón"]

# List containing the number of hours each worker worked.
hourList = [40, 50, 20, 23, 30, 42]

# List containing the hourly cost for each worker.
priceList = [35, 12, 22, 11, 14, 100]

# Loop for printing worker information
i = 0
while i < 6:

    print("The worker " + nameList[i] + " who worked " + str(hourList[i]) +
          " hours with an hourly cost of: $" + str(priceList[i]))

    # Increment the counter to move to the next element in the lists.
    i += 1
