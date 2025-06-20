class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2 

    @staticmethod
    def add(number1,number2):
        return f"Addition of the numbers is {number1 + number2}"
    
    @staticmethod
    def multiply(number1,number2):
        return f"Multiplication of the numbers is {number1 * number2}"
    
print(Calculator.add(2,4))
print(Calculator.multiply(5,7))