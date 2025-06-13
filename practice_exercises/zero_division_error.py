try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number"))

    division = num1 / num2
    print("Result", division)
except ZeroDivisionError:
        print("Cannot attempt to divide by zero. Enter a non zero number")