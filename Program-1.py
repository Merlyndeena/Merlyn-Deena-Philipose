a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add/sub/mul/div): ")

if op == "add":
    print("Result:", a + b)
elif op == "sub":
    print("Result:", a - b)
elif op == "mul":
    print("Result:", a * b)
elif op == "div":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
