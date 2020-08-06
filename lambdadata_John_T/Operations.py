"""Python program to perform Addition Subtraction Multiplication
and Division of two numbers"""


class calculator:
    def __init__(self, num1, num2, ch):
        self.num1 = int(input("Enter First Number: "))
        self.num2 = int(input("Enter Second Number: "))
        self.ch = input("Enter any of these char for specific operation +,-,*,/: ")
        if ch == '+':
            result = num1 + num2
            print(num1, ch, num2, ":", result)
        elif ch == '-':
            result = num1 - num2
            print(num1, ch, num2, ":", result)
        elif ch == '*':
            result = num1 * num2
            print(num1, ch, num2, ":", result)
        elif ch == '/':
            result = num1 / num2
            print(num1, ch, num2, ":", result)
        else:
            print("Input character is not recognized!")


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
