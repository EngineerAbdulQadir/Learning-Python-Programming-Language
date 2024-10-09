# Class 03 - Modules and pip in Python

## Table of Contents
1. [What is a Module?](#what-is-a-module)
2. [Types of Modules](#types-of-modules)
   - [1. Built-in Modules](#1-built-in-modules)
   - [2. External Modules](#2-external-modules)
3. [The pip Command](#the-pip-command)
4. [Using a Module in Python](#using-a-module-in-python)
5. [Next Lesson](#next-lesson)

## What is a Module?
A module is like a code library that allows us to use code written by somebody else in our Python program. 

## Types of Modules
There are two types of modules in Python:

### 1. Built-in Modules
These modules are ready to import, use, and come with the Python interpreter. There is no need to install such modules explicitly.

### 2. External Modules
These modules are imported from a third-party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of the same module over time.

## The pip Command
`pip` is a package manager that can be used to install Python modules. To install a module like `pandas`, you can use the following command:

```bash
pip install pandas
```

## Using a Module in Python
We use the `import` statement to import a module in Python. Here is an example code:

```python
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df)  # This will display the first few rows from the words.csv file
```

Similarly, we can install other modules and refer to their documentation for usage instructions. We will find ourselves doing this often in the later part of this course.

## Class 04
[Next Lesson>>](https://github.com/EngineerAbdulQadir/Learning-Python-Programming-Language/blob/main/Class%2004/Readme.md)