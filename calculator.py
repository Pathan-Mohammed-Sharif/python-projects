import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def sqrt(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    return math.sqrt(x)

def percentage(x, y):
    """Calculates x percent of y"""
    return (x / 100) * y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Percentage (x% of y)")

while True:
    choice = input("Enter choice (1/2/3/4/5/6) or 'q' to quit: ")

    if choice == 'q':
        print("ok bye")
        break

    if choice in ('1', '2', '3', '4', '6'):
        # Operations requiring two numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '6':
            print(f"{num1}% of {num2} = {percentage(num1, num2)}")

    elif choice == '5':
        # Operation requiring only one number
        try:
            num1 = float(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        result = sqrt(num1)
        print(f"Square Root of {num1} = {result}")

    else:
        print("Invalid Input")
