# Calculate Addition,Subtraction,Multiplication and Division from 2 numbers provided by user input.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

a = num1 + num2
b= num1 - num2
c= num1 * num2

if num2 != 0:
    d = num1 / num2
else:
    d= "Division by zero is undefined"

print(f"Sum: {num1} + {num2} = {a}")
print(f"Difference: {num1} - {num2} = {b}")
print(f"Product: {num1} * {num2} = {c}")
print(f"Division: {num1} / {num2} = {d}")
