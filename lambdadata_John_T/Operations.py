"""Python program to perform Addition Subtraction Multiplication
and Division of two numbers"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


class calculator(float):
    def __init__(self, x=None, y=None):
        super().__init__()
        self.y = y
        self.x = x

    # This function adds two numbers

    # This function subtracts two numbers

    # This function multiplies two numbers

    # This function divides two numbers

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("Invalid Input")


"""
class Math:
    def __init__(self):
        self.num1 = int(input("Enter First Number: "))
        self.num2 = int(input("Enter Second Number: "))
        self.ch = input("Enter any of these char for specific operation +,-,*,/: ")

    def Operation(self, num1, num2, ch):
        if ch == '+':
            result = num1 + num2
            return print(num1, ch, num2, ":", result)
        elif ch == '-':
            result = num1 - num2
            return print(num1, ch, num2, ":", result)
        elif ch == '*':
            result = num1 * num2
            return print(num1, ch, num2, ":", result)
        elif ch == '/':
            result = num1 / num2
            return print(num1, ch, num2, ":", result)
        else:
            return print("Input character is not recognized!") """

"""class calculator(float):
    def __init__(self, x=None, y=None):
        super().__init__()
        self.y = y
        self.x = x

    # This function adds two numbers
    def add(self, x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(self, x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(self, x, y):
        return x * y

    # This function divides two numbers
    def divide(self, x, y):
        return x / y

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("Invalid Input")"""