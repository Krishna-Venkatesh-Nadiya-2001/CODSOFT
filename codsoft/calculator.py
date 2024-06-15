def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

# Dictionary mapping operator symbols to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        operator = input("Enter operator (+, -, *, /): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operator in operations:
            result = operations[operator](num1, num2)
            print("Result:", result)
        else:
            print("Invalid operator")
    else:
        print("Invalid input")
        