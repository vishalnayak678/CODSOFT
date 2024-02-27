def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("A.Add")
print("B.Subtract")
print("C.Multiply")
print("D.Divide")

while True:
    choice = input("Enter choice(A/B/C/D): ")

    if choice in ('A', 'B', 'C', 'D'):
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'A':
            print(number1, "+", number2, "=", add(number1, number2))

        elif choice == 'B':
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif choice == 'C':
            print(number1, "*", number2, "=", multiply(number1, number2))

        elif choice == 'D':
            print(number1, "/", number2, "=", divide(number1, number2))

        next_calculation = input("Let's do next calculation? (positive/negetive): ")
        if next_calculation == "negetive":
          break
    else:
        print("Invalid Input")
