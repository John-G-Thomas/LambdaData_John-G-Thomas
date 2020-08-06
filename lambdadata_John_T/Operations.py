"""Python program to perform Addition Subtraction Multiplication
and Division of two numbers"""


def Operation(num1, num2, ch):
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
        return print("Input character is not recognized!")


class math:
    def __init__(self):
        self.num1 = int(input("Enter First Number: "))
        self.num2 = int(input("Enter Second Number: "))
        self.ch = input("Enter any of these char for specific operation +,-,*,/: ")


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
