# Class 06 - Variables and Data Types

## Table of Contents
1. [What is a Variable?](#what-is-a-variable)
2. [What is a Data Type?](#what-is-a-data-type)
    - [Numeric Data](#1-numeric-data)
    - [Text Data](#2-text-data)
    - [Boolean Data](#3-boolean-data)
    - [Sequenced Data](#4-sequenced-data)
        - [List](#list)
        - [Tuple](#tuple)
    - [Mapped Data](#5-mapped-data)
3. [Next Lesson](#next-lesson)

## What is a Variable?
A variable is like a container that holds data, similar to how kitchen containers hold sugar, salt, etc. Creating a variable is like reserving a placeholder in memory and assigning it some value.

In Python, it's as simple as writing:

```python
a = 1
b = True
c = "Harry"
d = None
```

These are four variables of different data types.

## What is a Data Type?
A data type specifies the kind of value a variable holds. It is essential in programming to perform operations without causing errors. In Python, you can print the type of a variable using the `type()` function:

```python
a = 1
print(type(a))  # Output: <class 'int'>
b = "1"
print(type(b))  # Output: <class 'str'>
```

Python provides the following built-in data types:

### 1. Numeric Data: `int`, `float`, `complex`

- **int**: Integer values like `3`, `-8`, `0`
- **float**: Floating-point values like `7.349`, `-9.0`, `0.0000001`
- **complex**: Complex numbers like `6 + 2i`

### 2. Text Data: `str`

- **str**: Strings or text values, such as `"Hello World!!!"` or `"Python Programming"`

### 3. Boolean Data

Boolean data consists of the values `True` or `False`.

### 4. Sequenced Data: `list`, `tuple`

- **List**: A list is an ordered collection of elements, separated by commas and enclosed within square brackets `[]`. Lists are mutable, meaning they can be modified after creation.

**Example:**
```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```

**Output**:
```
[8, 2.3, [-4, 5], ['apple', 'banana']]
```

- **Tuple**: A tuple is an ordered collection of elements, separated by commas and enclosed within parentheses `()`. Tuples are immutable, meaning they cannot be modified after creation.

**Example:**
```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```

**Output**:
```
(('parrot', 'sparrow'), ('Lion', 'Tiger'))
```

### 5. Mapped Data: `dict`

- **Dictionary**: A dictionary is an unordered collection of key-value pairs, where each key is unique. The key-value pairs are enclosed within curly brackets `{}`.

**Example:**
```python
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)
```

**Output**:
```
{'name': 'Sakshi', 'age': 20, 'canVote': True}
```

## Class 07
[Next Lesson>>](https://replit.com/@codewithharry/07-Day7-Exercise-1-Create-a-Calculator)