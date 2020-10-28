def addition(a,b):
    a = float(a)
    b = float(b)
    return a+b

class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a,b)
        return addition(a,b)

    def __init__(self):
        pass