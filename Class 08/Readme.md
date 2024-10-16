# Class 08 - Calculator Solution

## Table of Contents
1. [Exercise Description](#exercise-description)
2. [Solution Code](#solution-code)
3. [Explanation](#explanation)
4. [Next Lesson](#next-lesson)

## Exercise Description
Create a calculator that can perform the following operations on two numbers:
- Addition
- Subtraction
- Multiplication
- Division

Your program should format the output in a readable manner!

## Solution Code
```python
# Getting user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Printing the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
```

## Explanation
In this program:
1. The user is prompted to enter two numbers. These numbers are stored as floating-point values (`float`) to allow for decimal operations.
2. The program performs four arithmetic operations: addition, subtraction, multiplication, and division.
3. Division by zero is handled to avoid errors, displaying a message instead of performing the operation when the second number is zero.
4. The results are printed in a formatted, readable manner.

## Class 09
[Next Lesson >>](https://replit.com/@codewithharry/09-Day9-Typecasting-in-Python)