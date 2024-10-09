# Class 05 - Comments, Escape Sequence & Print in Python

## Table of Contents
1. [Introduction](#introduction)
2. [Python Comments](#python-comments)
    - [Single-Line Comments](#single-line-comments)
    - [Multi-Line Comments](#multi-line-comments)
3. [Escape Sequence Characters](#escape-sequence-characters)
4. [More on Print Statement](#more-on-print-statement)
5. [Next Lesson](#next-lesson)

## Introduction
Welcome to Class 05 of the Python learning series. Today, we will dive into Comments, Escape Sequences, and additional details about the `print()` statement in Python.

## Python Comments
A comment is a part of the code that the programmer does not want to execute. Instead, it's used to explain parts of the code or prevent certain parts of the code from being executed during testing.

### Single-Line Comments
Single-line comments start with a `#` symbol.

#### Example 1
```python
# This is a 'Single-Line Comment'
print("This is a print statement.")
```
**Output**:
```
This is a print statement.
```

#### Example 2
```python
print("Hello World !!!") # Printing Hello World
```
**Output**:
```
Hello World !!!
```

#### Example 3
```python
print("Python Program")
# print("Python Program")
```
**Output**:
```
Python Program
```

### Multi-Line Comments
For multi-line comments, you can either use multiple `#` symbols or a multiline string (`"""`).

#### Example 1: Using `#`
```python
# It will execute a block of code if a specified condition is true.
# If the condition is false, it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```
**Output**:
```
p is greater than 5.
```

#### Example 2: Using Multiline String
```python
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```
**Output**:
```
p is greater than 5.
```

## Escape Sequence Characters
To insert characters that cannot be directly used in a string, we use escape sequences. These sequences start with a backslash (`\`).

#### Example:
```python
print("This doesn't \"execute\" properly.")
```
**Output**:
```
This doesn't "execute" properly.
```

## More on Print Statement
The `print()` function is commonly used to display output. Its syntax looks like this:

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

### Parameters of `print()`:
1. **object(s)**: Any object to print (multiple objects can be provided, separated by commas).
2. **sep**: Specifies how to separate the objects (default is a space `' '`).
3. **end**: Specifies what to print at the end (default is `'\n'`).
4. **file**: An object with a write method (default is `sys.stdout`).

Parameters 2 to 4 are optional and allow flexibility in formatting output.

## Class 06
[Next Lesson>>](https://replit.com/@codewithharry/06-Day6-Variables-and-Data-Types)