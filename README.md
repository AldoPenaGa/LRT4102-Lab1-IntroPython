<p align="center">
  <h2 align="center">Intro to Python and Github</h2>

  <p align="justify">
  This is the initial lab report for the course titled Robotic Systems Design (LRT4102). This report will serve as an introduction to the Python programming language.
	  
  <br>Universidad de las Américas Puebla - Prof. Dr. César Martínez Torres. "https://www.linkedin.com/in/c%C3%A9sar-martinez-torres-617b5347/?originalSubdomain=mx>" 
  </p>
</p>
<be>

## Table of contents
- [Introduction](#introduction)
- [Problems](#problems)
- [Codes](#codes)

<div align= "justify">

### Introduction
Python is a high-level, interpreted, dynamic programming language. Python's design philosophy promotes the readability of code by the use of strong indentation. It supports a variety of programming paradigms, including structured (specifically procedural), object-oriented, and functional programming. Python is one of today's most popular and quickly growing programming languages. It is commonly used in scientific computing, data analysis, machine learning, artificial intelligence, robotics applications, web development, and network servers. Python's simplicity has encouraged many developers to create new machine-learning packages, making it a popular language for artificial intelligence.

</div>

Some of the most basic structures used in Python are:

1. Variables: Python supports several types of variables. 
   - Integers: These are positive or negative whole numbers with no decimal point. Example:
     -  x = 5
   - Floats: These are real numbers with a decimal point. Example:
     -  y = 30.7
   - Strings: These are sequences of characters. Example:
     - name = "Robotics".
   - Booleans: These represent if the variable is either True or False. Example:
     - a = True
   - Complex: These are numbers with a real and imaginary component represented as x + yj. Example:
     - b = 1 + 2j

<div align= "justify">
	
It is necessary to distinguish between local and global variables, Python global variables are those that are not declared inside any function and have a global scope, whereas Python local variables are those that are created inside a function and their scope is confined to that function alone.

</div>


2. Basic Math Operations: Python supports a variety of mathematical operations. Example:

```python
x = 10
y = 20

print(x + y)  # Addition

print(x - y)  # Subtraction

print(x * y)  # Multiplication

print(x / y)  # Division

print(x % y)  # Modulus

print(x ** y) # Exponentiation

print(x // y) # Floor division

```

<div align= "justify">
	
3. Lists: A list in Python is a collection of elements that can be of any kind. The elements in a list are contained in square brackets [ ] and separated by commas. You may modify the content of a list without restrictions. You can access list items by referring to the index number. Python lists index always starts from 0. Example:

</div>

```python
my_list = [1, 2, "Py", 3.4]
print(my_list[0])  # Output: 1
```
<div align= "justify">

4. Tuples: They are similar to lists. The distinction between the two is that after a tuple has been established, its elements cannot be modified, but as how we stated, items in a list can be. A tuple is formed by wrapping all of the elements in parenthesis (), separated by commas. Example:

</div>

```python
my_tuple = ("systems", 2, "Design", 4.5)
print(my_tuple[0])  # Output: systems
```

<div align= "justify">

5. Dictionaries: It is an unordered collection of items. Each item has a key/value pair. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value. Example:

</div>

```python
my_dict = {"brand": "UniversalRobots", "model": "UR5", "year": 2017}
print(my_dict["brand"])  # Output: UniversalRobots
```
<div align= "justify">

6. If Condition: Python supports the usual logical conditions from maths. These conditions can be used in many ways, most commonly in “if statements” and loops. Example:

</div>

```python
x = 10
y = 20

if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y")
```
<div align= "justify">

7. For loop: The for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. Example:

</div>

```python
for i in range(5):
    print(i)
```
<div align= "justify">

8. While loop: The while loop is used to iterate as long as the test expression (condition) is true. Example:

</div>

```python
i = 0
while i < 5:
	print(i)
	i += 1
```

### Problems

<div align= "justify">

The following problems were asked :
1. Create a list named 'numbers' that contain at least 10 numbers, then calculate the average of the even numbers and the product of the odd numbers. Finally, print the results.
   
3. Design a program that prompts the user to guess a secret number. The program should generate a random number between 1 and 10, and the user should attempt to guess it. If the user’s guess is too high or too low, the program should provide hints. The while loop should continue until the user correctly guesses the number. At the end, the program should print how many attempts it took for the user to guess the number correctly.
   
4. The program should generate a matrix of at least 5x5. The robot begins its journey at the (0,0) position of the matrix and must exit at the (4,4) position or the maximum position if the matrix size is changed. The number and position of the obstacles are random. The robot can only move forward, turn left or right to find a free path. In the event that the robot cannot exit, it should print on the screen ‘Unable to reach the destination’. If the robot reaches its final destination, it should print the map, with the free spaces and obstacles in the following format: X for obstacle and o for free space. Alike:

</div>

<div align="center">
  
| o o o X o |
|-----------|
| o o o o o |
| o o o o X |
| o o o o o |
| o X X X o |

</div>

It should also print the route it followed. Display a second map with the ‘path’ followed by the robot using arrows.

### Codes

**Week 1**

*BarsCost.py*
```python
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
```
This Python script calculates and displays the cost of sold and non-fresh bars.

*Lists.py*
```python
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
```
This code prints the information of each worker from a list. 

*SimpleMath.py*
```python
# Asks user to input an n term
n = int(input("Enter n: "))

# Does the operation
operation = (n *(n + 1))/2

# Prints it
print(str(operation))
```
It solves a simple math operation: (n *(n + 1))/2 where it asks the user for the term n.

*WeeklyPay.py*
```python

# Gets the hours worked
hours = int(input("Enter the number of hours worked: "))

# Gets the cost per hour
cost = int(input("Enter the cost per hour: "))

# Does the math
total = hours * cost

# Prints it
print(str(total))
```
It gives the total amount of money that a worker would get according to their salary per hour.

**Week 2**
*Guesser.py*
```python
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
```
It asks the user to guess a number randomly selected from a list that goes from 1 to 10.

*Numbers.py*
```python
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

```
This python script forms a list called ‘numbers’ with 10+ elements, that computes the even numbers’ average and odd numbers’ product, then it displays the outcomes.

*Obstacles.py*
```python
# Dependencies
import random
import numpy as np

## MATRIX

# Setting up the minimum size of the matrix
mSize = 0
while mSize < 5:

    mSize = int(input("Enter the size of the wishable size for the matrix: ")) # Asking user

    if mSize < 5:
        print("The matrix should be at least of 5 x 5") # Indicating user it should be from at least 5x5

# Setting up the matrixes

m = np.zeros((mSize, mSize), dtype=str) # main matrix
d = m # directions matrix (the one whc¡ich will contain the arrows)

# Start-up of the matrixes
for i in range(mSize):
    for j in range(mSize):
        m[i, j] = random.choice(['x', 'o', 'o'])

# Setting up the starting and finish points

m[0, 0] = 'R' # R of Robot
m[mSize - 1, mSize - 1] = 'D' # D of Destination

print("Initial Matrix:")
print(m)

## NAVIGATION

attempts = 0

if m[0, 1] == 'x' and m[1, 0] == 'x':
    print("No valid path exists from the beginning.") # Because it happened that it wanted to keep following

else:

    # Setting up special navigation parameters

    current_row, current_col = 0, 0
    last_origin_row = 0
    # If it hasn't got to the boundary then: 

    while (current_row, current_col) != (mSize - 1, mSize - 1):
        attempts += 1  # Increment attempts

        # RIGHT

        # It checks the following facts:
            # Is it inside a boundary in x? If yes, proceed.
            # Is there space left to the right or has it moved to that position before? If yes, proceed.
            # Is there an obstacle there?  If not, proceed.
        
        if current_col < mSize - 1 and (m[current_row][current_col + 1] == 'o' or m[current_row][current_col + 1] == 'M') and m[current_row][current_col + 1] != 'x':
            
            m[current_row][current_col] = 'M' # Writing in main matrix.
            d[current_row][current_col] = '→' # Writing in directions matrix.

            current_col += 1

            print(m)
            print("Moving right")
        
        # DOWN

        # It checks the following facts:
            # Is it inside a boundary in y? If yes, proceed.
            # Is there space left to the down side or has it moved to that position before? If yes, proceed.
            # Is there an obstacle there?  If not, proceed.

        elif current_row < mSize - 1 and (m[current_row + 1][current_col] == 'o' or m[current_row + 1][current_col] == 'M') and m[current_row + 1][current_col] != 'x':
            
            m[current_row][current_col] = 'M' # Writing in main matrix.
            d[current_row][current_col] = '↓' # Writing in directions matrix.

            current_row += 1

            print(m)
            print("Moving down")

        # If it is in the last row or last column and the destination is nearby, then proceed.

        elif (current_col == mSize - 1 or current_row == mSize - 1) and \
                ((current_row + 1 < mSize and m[current_row + 1][current_col] == 'D') or \
                (current_col + 1 < mSize and m[current_row][current_col + 1] == 'D')):
            
            # Move down or right if 'D' is at the destination and the robot is at the final column or row
            m[current_row][current_col] = 'M'

            # Reaching destination Down.
            if current_row + 1 < mSize and m[current_row + 1][current_col] == 'D':
                d[current_row][current_col] = '↓'  # Writing in directions matrix
                current_row += 1

                print(m)
                print("Moving to the destination down")

            # Reaching destination right.
            else:
                d[current_row][current_col] = '→'  # Writing in directions matrix
                current_col += 1

                print(m)
                print("Moving to the destination right")
        
        # None of the cases above (because the robot cannot continue in that path):

        else:

            last_origin_row += 1 #Updating this helper.

            if last_origin_row < mSize:  # Ensure the helper is within the matrix bounds (it gave problems when it wasn't).

                current_row, current_col = last_origin_row, 0 # Updating the parameters so the robot can begin again.

                print(m)
                print("Unable to move right or down. Stepping back to row after the origin and restarting.")

                print("Current position:", current_row, current_col) # Describing the new parameters.
            else:

                # In case there is no path to follow and we already reached the end of the matrix, there is nothing left to do so:

                print("No valid path exists.")
                break

    # But it the robot reached its destination (which is in the final boundaries), then print it, let's celebrate.

    if (current_row, current_col) == (mSize - 1, mSize - 1):
        print(m)
        print("Robot reached the destination!")

# Final printings

print("Final Matrix:")
print(d)
print("The robot did a total of: " + str(attempts) + " moves.")

```
This final script initially prepares the surroundings for the robot's the crossing. It generate random numbers and adjust matrices. It then asks the user to set the grid size, which must be at least 5x5 in order to function properly. Next, the algorithm makes two matrices: the main matrix (m) represents the real grid where the robot walks, and the directions matrix (d) keeps track of the robot's journey. The primary matrix is originally composed of empty spaces ('o'), barriers ('x'), the starting point ('R'), and the destination ('D'). The robot starts in the top-left corner (0, 0) and aims to reach the bottom-right corner (mSize - 1, mSize - 1). 

The navigation logic then takes control. The code maintains track of the robot's present position, the number of moves it has performed, and a helper variable to aid with retracing. It checks to see if the robot is obstructed from the start, stopping it from beginning its route. The key to navigation occurs within a loop. The code repeatedly attempts to drive the robot in the intended direction (right first, then down) as long as it remains inside the grid borders, has not visited the same location before, and is not obstructed by an obstacle. If neither way is viable, the robot intelligently returns to a prior place and attempts an alternative route. However, if even backtracking fails, the programming decides that the robot has no viable path to reach its target.

Finally, if the robot successfully navigates the maze and reaches its destination, the code shows the end state of both the main matrix and the directions matrix, displaying the robot's directions followed. It also notifies the user of the number of moves the robot took to achieve its goal.

### Contributors

| Name                          | ID   | Github                               |
|-------------------------------|--------|--------------------------------------|
| Aldo Oziel Peña Gamboa        | 169382 | https://github.com/AldoPenaGa        |
