import random

numbers = [1,2,3,4,5,6,7,8,9,10]
num = random.choice(numbers)
#print(num)

counter = 0
guess = 0

print("You will be asked to ask a secret number, it is random from 1 to 10, hints will be provided if you're too high or two low.")

while guess != num:
    guess = int(input("Enter the number you think will be the right guess: "))
    cocient = guess/num 

    if cocient < 1:
        print ("The correct number is higher than the guess")

    elif cocient > 1:
        print("THe correct number is lower than the guess")

    elif cocient == 1:
        print("Correct guess!, the number of attempts was: " + str(counter))

    counter +=1 


