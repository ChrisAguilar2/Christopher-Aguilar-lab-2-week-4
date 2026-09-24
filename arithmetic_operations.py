#Christopher Aguilar
#CMP 131
#Basic Arithmetic Operations Week 4 Lab 2
#September 22, 2026

# Program title
print("==============================")
print("Basic Arithmetic Operations")
print("==============================")

# User input
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Arithmetic calculation 
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
power = first_number ** second_number
average = (first_number + second_number) / 2

# Output
print("First Number: ", first_number)
print("Second Number :", second_number)
print(f"Addittion:  {addition:.2f}")
print(f"Subtraction:  {subtraction:.2f}")
print(f"Multiplication:  {multiplication:.2f}")
print(f"Division:  {division:.2f}")
print(f"Power:  {power:.2f}")
print(f"Average:  {average:.2f}")
