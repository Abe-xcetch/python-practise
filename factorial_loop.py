# Task: Compute factorial using a loop
# Thought process: Start from 1 and multiply each number up to the target number.

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial of", number, "is", factorial)
