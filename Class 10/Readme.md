# Class 10 - Taking User Input in Python

## Table of Contents
1. [Taking User Input](#taking-user-input)
2. [Typecasting User Input](#typecasting-user-input)
3. [Displaying Custom Text with Input](#displaying-custom-text-with-input)
4. [Example Code](#example-code)
5. [Next Lesson](#next-lesson)

## Taking User Input
In Python, you can take user input directly using the `input()` function. The value returned by this function is always a string (character-based). To store this input in a variable, you simply assign it as follows:

### Syntax:
```python
variable = input()
```

## Typecasting User Input
Since the `input()` function always returns a string, you need to explicitly convert the input into the desired data type (e.g., integer, float) using typecasting functions when necessary.

### Example:
```python
variable = int(input())  # Typecasts input to integer
variable = float(input())  # Typecasts input to float
```

## Displaying Custom Text with Input
The `input()` function can also display a message prompting the user for input. This can be helpful in guiding the user on what to enter.

### Example:
```python
a = input("Enter the name: ")
print(a)
```

### Output:
```
Enter the name: Abdul Qadir
Abdul Qadir
```

## Example Code
```python
# Asking for user input and printing it
a = input("Enter your name: ")
print("My name is", a)

# Taking two numbers as input
x = input("Enter first number: ")
y = input("Enter second number: ")

# Adding the inputs as strings (concatenation)
print(x + y)

# Adding the inputs as integers
print(int(x) + int(y))
```

### Explanation:
1. The first part of the code asks for the user's name and prints it.
2. The second part takes two numbers as input and demonstrates both string concatenation and integer addition.

## Class 11
[Next Lesson >>]()