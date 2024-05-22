# PART1
# Function to add two numbers
def add_two_numbers(num1, num2):
    return num1 + num2

# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Add the two numbers
result = add_two_numbers(num1, num2)

# Print the result
print(f"The sum of {num1} and {num2} is {result}")


# Function to subtract two numbers
def subtract_two_numbers(num1, num2):
    return num1 - num2

# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Subtract the two numbers
result = subtract_two_numbers(num1, num2)

# Print the result
print(f"The result of subtracting {num2} from {num1} is {result}")


#PART2
# Function to multiply two numbers
def multiply_two_numbers(num1, num2):
    return num1 * num2

# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Multiply the two numbers
result = multiply_two_numbers(num1, num2)

# Print the result
print(f"The product of {num1} and {num2} is {result}")



# Function to divide two numbers
def divide_two_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2

# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Divide the two numbers
result = divide_two_numbers(num1, num2)

# Print the result
print(f"The result of dividing {num1} by {num2} is {result}")
