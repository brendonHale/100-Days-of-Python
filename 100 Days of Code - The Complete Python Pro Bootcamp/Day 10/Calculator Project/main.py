import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# print(operations['*'](4, 8))

def calculator():
    print(art.logo)
    previous = True
    num1 = float(input("Enter first number: "))

    while previous:
        for symbol in operations:
            print(symbol)
        operation = input("Enter operation: ")
        num2 = float(input("Enter second number: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        choice = input("Would you like to continue using previous answer? (y/n): ")

        if choice == "y":
            num1 = answer
        else:
            previous = False
            print("\n * 20")
            calculator()

calculator()