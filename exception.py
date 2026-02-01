# 1. Script to create an ArithmeticError
a = 10
b = 0
print(a / b)   # Division by zero creates ArithmeticError


# 2. Script to create a ValueError
num = int("abc")   # Invalid conversion creates ValueError


# 3. Script to handle ArithmeticError
try:
    x = 10
    y = 0
    print(x / y)
except ArithmeticError:
    print("Arithmetic Error occurred")


# 4. Script to handle ValueError
try:
    num = int("xyz")
except ValueError:
    print("Value Error occurred")


# 5. Script to handle multiple exceptions in one try
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ValueError:
    print("Value Error occurred")
except ArithmeticError:
    print("Arithmetic Error occurred")


# 6. Script to create a calculator with 4 basic operations and handle exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

except ValueError:
    print("Please enter valid integers")
except ArithmeticError:
    print("Cannot divide by zero")


# 7. Script with finally block (calculator example)
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division:", a / b)
except ValueError:
    print("Invalid input")
except ArithmeticError:
    print("Division by zero error")
finally:
    print("Calculator program executed")


# 8. Script using try, except and else block for division
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ArithmeticError:
    print("Division error")
else:
    print("Result:", result)


# 9. Script to raise a ValueError
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")
else:
    print("Eligible")


# 10. Script to implement nested try-except block
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    try:
        print(a / b)
    except ArithmeticError:
        print("Inner block: Division by zero")
except ValueError:
    print("Outer block: Invalid input")
