"""Python program to perform Addition Subtraction Multiplication
and Division of two numbers"""


class calculator(float):
    def __init__(self, num1=None, num2=None):
        super().__init__()
        self.num2 = num2
        self.num1 = num1

    # This function adds two numbers
    def add(self, y):
        return self + y

    # This function subtracts two numbers
    def subtract(self, y):
        return self - y

    # This function multiplies two numbers
    def multiply(self, y):
        return self * y

    # This function divides two numbers
    def divide(self, y):
        return self / y

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
                print(num1, "+", num2, "=", add(num1))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1))
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
