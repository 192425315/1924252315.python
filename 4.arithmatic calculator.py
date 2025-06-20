def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): 
    if b == 0:
        return "Error! Division by zero."
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print("Result:", add(a, b))
elif operator == '-':
    print("Result:", subtract(a, b))
elif operator == '*':
    print("Result:", multiply(a, b))
elif operator == '/':
    print("Result:", divide(a, b))
else:
    print("Invalid operator")
