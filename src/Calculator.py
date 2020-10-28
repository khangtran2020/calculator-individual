import math

def addition(a,b):
    a = float(a)
    b = float(b)
    return a+b

def subtraction(a,b):
    a = float(a)
    b = float(b)
    return a - b

def multiplication(a,b):
    a = float(a)
    b = float(b)
    return a*b

def division(a,b,c):
    a = float(a)
    b = float(b)
    if (b == 0):
        return None
    else:
        return round(a/b,c)

def squaring(a):
    a = float(a)
    return a**2

def squareRoot(a,b):
    a = float(a)
    if (a<0):
        return None
    else:
        return round(math.sqrt(a),b)

class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a,b)
        return addition(a,b)

    def subtract(self, a, b):
        self.result = subtraction(b,a)
        return subtraction(b,a)

    def multiply(self, a, b):
        self.result = multiplication(a,b)
        return multiplication(a,b)

    def divide(self, a, b, c):
        self.result = division(b,a,c)
        return division(b,a,c)

    def square(self, a):
        self.result = squaring(a)
        return squaring(a)

    def sqrt(self, a, b):
        self.result = squareRoot(a,b)
        return squareRoot(a, b)

    def __init__(self):
        pass