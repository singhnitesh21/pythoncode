# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
addition_result = num1 + num2
print("Addition:", num1, "+", num2, "=", addition_result)

# Subtraction
subtraction_result = num1 - num2
print("Subtraction:", num1, "-", num2, "=", subtraction_result)


# Division
if num2 != 0:  # Avoid division by zero
    division_result = num1 / num2
    print("Division:", num1, "/", num2, "=", division_result)
else:
    print("Division by zero is not allowed.")

#CODE by BUNTY
