def addition(a,b):
    a = float(a)
    b = float(b)
    return a+b

def subtraction(a,b):
    a = float(a)
    b = float(b)
    return a - b

class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a,b)
        return addition(a,b)

    def subtract(self, a, b):
        self.result = subtraction(b,a)
        return subtraction(b,a)

    def __init__(self):
        pass