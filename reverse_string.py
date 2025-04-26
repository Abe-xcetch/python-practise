# Task: Reverse a string without using [::-1] or built-in methods
# Thought process: Start from last character, keep adding to new string.

text = "hello"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)
