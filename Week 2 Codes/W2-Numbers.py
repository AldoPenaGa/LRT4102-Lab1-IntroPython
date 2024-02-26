# Define a list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 20]

# Varaibles

sumEven = 0  # To store the sum of even numbers
counterEven = 0  # To count the number of even numbers
productOdd = 1  # To store the product of odd numbers

# Loop through each number in the list
for i in numbers:

    # Check if the number is even using the module operator (%)
    test = i % 2

    # Process even numbers
    if test == 0:
        numType = "even"  # Assign the number type for clarity

        # Add the even number to the sum and increment the counter
        sumEven += i
        counterEven += 1

        # Calculate the average of even numbers (avoid division by zero)
        if counterEven > 0:
            avgEven = sumEven / counterEven
        else:
            avgEven = "No even numbers to calculate the average."  # Informative message

    # Process odd numbers
    else:
        numType = "odd"  # Assign the number type for clarity

        # Multiply the odd number to the product
        productOdd *= i

# Print the results
print("The average of the even numbers is: " + str(avgEven))
print("The product of the odd numbers is: " + str(productOdd))



