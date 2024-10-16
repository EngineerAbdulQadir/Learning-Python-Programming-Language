# Class 07 - Operators

## Table of Contents
1. [What are Operators?](#what-are-operators)
2. [Types of Operators](#types-of-operators)
    - [Arithmetic Operators](#arithmetic-operators)
3. [Exercise](#exercise)
    - [Exercise 1 - Create a Calculator](#exercise-1-create-a-calculator)
4. [Explanation](#explanation)
5. [Next Lesson](#next-lesson)

## What are Operators?
Operators in Python are special symbols used to perform operations on variables and values. They are essential for performing calculations, comparisons, and logical tasks.

In this lesson, we focus on arithmetic operators, which allow us to perform basic mathematical operations like addition, subtraction, multiplication, and more.

## Types of Operators

### Arithmetic Operators

|   Operator  | Operator Name      | Example          |
|-------------|--------------------|------------------|
| `+`         | Addition            | `15 + 7`         |
| `-`         | Subtraction         | `15 - 7`         |
| `*`         | Multiplication      | `5 * 7`          |
| `**`        | Exponential         | `5 ** 3`         |
| `/`         | Division            | `5 / 3`          |
| `%`         | Modulus             | `15 % 7`         |
| `//`        | Floor Division      | `15 // 7`        |

These operators are vital for numerical operations, especially when creating tools like calculators.

## Exercise

Below is an example program using arithmetic operators:

```python
n = 15
m = 7

ans1 = n + m
print("Addition of", n, "and", m, "is", ans1)

ans2 = n - m
print("Subtraction of", n, "and", m, "is", ans2)

ans3 = n * m
print("Multiplication of", n, "and", m, "is", ans3)

ans4 = n / m
print("Division of", n, "and", m, "is", ans4)

ans5 = n % m
print("Modulus of", n, "and", m, "is", ans5)

ans6 = n // m
print("Floor Division of", n, "and", m, "is", ans6)
```

### Exercise 1 - Create a Calculator
Create a calculator capable of performing addition, subtraction, multiplication, and division operations on two numbers. Your program should format the output in a readable manner!

## Explanation
- `n` and `m` store the values `15` and `7`, respectively.
- The variables `ans1`, `ans2`, `ans3`, `ans4`, `ans5`, and `ans6` hold the results of the addition, subtraction, multiplication, division, modulus, and floor division operations.
- The program uses arithmetic operators to perform these operations, and the results are printed in a readable format.

## Next Lesson
[Next Lesson>>](https://replit.com/@codewithharry/08-Day8-Exercise-1-Create-a-Calculator-Solution#main.py)