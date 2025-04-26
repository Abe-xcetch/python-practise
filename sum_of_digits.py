# Task: Sum of digits of a number
# Thought process: Extract digits using modulus (%) and integer division (//).

number = 12345
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10

print("Sum of digits:", sum_of_digits)
