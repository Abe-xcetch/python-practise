# Task: Compute factorial using recursion
# Thought process: Function calls itself until reaching 1.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
print("Factorial of", number, "is", factorial(number))
