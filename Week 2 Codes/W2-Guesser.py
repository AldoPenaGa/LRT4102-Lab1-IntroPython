# Dependencies
import random

# Generate a random number between 1 and 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = random.choice(numbers)

# Initialize variables
counter = 0
guess = 0

# Explanation
print("You will be asked to ask a secret number, it is random from 1 to 10, hints will be provided if you're too high or two low.")

# Guessing loop
while guess != num:
    # Get user input
    guess = int(input("Enter the number you think will be the right guess: "))

    # Check if guess is too low, too high, or correct
    cocient = guess/num 

    # Use "if" statements for different conditions 
    if cocient < 1:  # If guess is lower than the secret number
        print ("The correct number is higher than the guess")

    elif cocient > 1:  # If guess is higher than the secret number
        print("The correct number is lower than the guess")

    # Success condition
    elif cocient == 1:  # If guess is equal to the secret number
        print("Correct guess!, the number of attempts was: " + str(counter))

    # Increment counter for number of attempts
    counter +=1 
