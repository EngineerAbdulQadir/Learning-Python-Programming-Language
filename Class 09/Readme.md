# Class 09 - Typecasting in Python

## Table of Contents
1. [What is Typecasting?](#what-is-typecasting)
2. [Types of Typecasting](#types-of-typecasting)
   - [Explicit Conversion](#explicit-conversion-explicit-type-casting-in-python)
   - [Implicit Conversion](#implicit-conversion-implicit-type-casting-in-python)
3. [Examples of Typecasting](#examples-of-typecasting)
   - [Explicit Typecasting Example](#example-of-explicit-typecasting)
   - [Implicit Typecasting Example](#example-of-implicit-type-casting)
4. [Next Lesson](#next-lesson)

## What is Typecasting?
Typecasting (or type conversion) is the process of converting one data type into another. In Python, this can be done using built-in functions like `int()`, `float()`, `str()`, and many more.

## Types of Typecasting
Python supports two types of typecasting:
1. **Explicit Conversion (Manual)**
2. **Implicit Conversion (Automatic)**

### Explicit Conversion (Explicit Type Casting in Python)
This type of typecasting is performed manually by the developer using Python’s built-in functions such as `int()`, `float()`, `str()`, etc. It allows you to convert one data type into another as per the program’s requirements.

#### Example of explicit typecasting:
```python
string = "15"
number = 7
string_number = int(string)  # Converts string to integer
sum = number + string_number
print("The sum of both the numbers is:", sum)
```
**Output:**
```
The sum of both the numbers is: 22
```

### Implicit Conversion (Implicit Type Casting in Python)
Python automatically handles implicit conversions when combining variables of different data types. This type of conversion is done to prevent data loss, where Python automatically converts smaller data types (e.g., `int`) to larger types (e.g., `float`).

#### Example of implicit type casting:
```python
# Python automatically converts a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float for the addition
c = a + b
print(c)
print(type(c))
```
**Output:**
```
<class 'int'>
<class 'float'>
10.0
<class 'float'>
```

## Class 10
[Next Lesson >>]()