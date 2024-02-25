<p align="center">
  <h2 align="center">Intro to Python and Github</h2>

  <p align="center">
  This is the initial lab report for the course titled Robotic Systems Design (LRT4102). This report will serve as an introduction to the Python programming language.
  <br>Universidad de las Américas Puebla - Prof. Dr. César Martínez Torres. "https://www.linkedin.com/in/c%C3%A9sar-martinez-torres-617b5347/?originalSubdomain=mx>" 
  </p>
</p>
<br>

## Table of contents
- [Introduction](#introduction)
- [Problems](#problems)
- [Codes](#codes)


### Introduction
Python is a high-level, interpreted, dynamic programming language. Python's design philosophy promotes the readability of code by the use of strong indentation. It supports a variety of programming paradigms, including structured (specifically procedural), object-oriented, and functional programming. Python is one of today's most popular and quickly growing programming languages. It is commonly used in scientific computing, data analysis, machine learning, artificial intelligence, robotics applications, web development, and network servers. Python's simplicity has encouraged many developers to create new machine-learning packages, making it a popular language for artificial intelligence.

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


It is necessary to distinguish between local and global variables, Python global variables are those that are not declared inside any function and have a global scope, whereas Python local variables are those that are created inside a function and their scope is confined to that function alone.

2. Basic Math Operations: Python supports a variety of mathematical operations. Example:

x = 10
y = 20

print(x + y)  # Addition

print(x - y)  # Subtraction

print(x * y)  # Multiplication

print(x / y)  # Division

print(x % y)  # Modulus

print(x ** y) # Exponentiation

print(x // y) # Floor division

3. Lists: A list in Python is a collection of elements that can be of any kind. The elements in a list are contained in square brackets [ ] and separated by commas. You may modify the content of a list without restrictions. You can access list items by referring to the index number. Python lists index always starts from 0. Example:

  - my_list = [1, 2, "Py", 3.4]
    - rint(my_list[0])  # Output: 1

4. Tuples: They are similar to lists. The distinction between the two is that after a tuple has been established, its elements cannot be modified, but as how we stated, items in a list can be. A tuple is formed by wrapping all of the elements in parenthesis (), separated by commas. Example:

  - my_tuple = ("systems", 2, "Design", 4.5)
    - print(my_tuple[0])  # Output: Systems
   
5. Dictionaries: It is an unordered collection of items. Each item has a key/value pair. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value. Example:

  - my_dict = {"brand": "UniversalRobots", "model": "UR5", "year": 2017}
    - print(my_dict["brand"])  # Output: UniversalRobots
    
6. If Condition: Python supports the usual logical conditions from maths. These conditions can be used in many ways, most commonly in “if statements” and loops. Example:

x = 10
y = 20

if x < y:

    print("x is less than y")
    
elif x == y:

    print("x is equal to y")
    
else:

    print("x is greater than y")

7. For loop: The for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. Example:

for i in range(5):

    print(i)

8. While loop: The while loop is used to iterate as long as the test expression (condition) is true. Example:

i = 0

while i < 5:

    print(i)
    
    i += 1

### Problems
The following problems were asked :
1. Create a list named 'numbers' that contain at least 10 numbers, then calculate the average of the even numbers and the product of the odd numbers. Finally, print the results.
   
3. Design a program that prompts the user to guess a secret number. The program should generate a random number between 1 and 10, and the user should attempt to guess it. If the user’s guess is too high or too low, the program should provide hints. The while loop should continue until the user correctly guesses the number. At the end, the program should print how many attempts it took for the user to guess the number correctly.
   
4. The program should generate a matrix of at least 5x5. The robot begins its journey at the (0,0) position of the matrix and must exit at the (4,4) position or the maximum position if the matrix size is changed. The number and position of the obstacles are random. The robot can only move forward, turn left or right to find a free path. In the event that the robot cannot exit, it should print on the screen ‘Unable to reach the destination’. If the robot reaches its final destination, it should print the map, with the free spaces and obstacles in the following format: X for obstacle and o for free space. Alike:

<p align="center">
  
| o o o X o |
|-----------|
| o o o o o |
| o o o o X |
| o o o o o |
| o X X X o |

</p>

It should also print the route it followed. Display a second map with the ‘path’ followed by the robot using arrows.

### Codes



### Contributors

| Name                          | ID   | Github                               |
|-------------------------------|--------|--------------------------------------|
| Aldo Oziel Peña Gamboa        | 169382 | https://github.com/AldoPenaGa        |
