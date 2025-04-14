def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number!")
    return a ** 0.5


class Calculator:
    def __init__(self,initial_value=0):
        self.initial_value = initial_value
        # Optional: Store initial value if needed
        self.memory = 0  # Optional: Store previous result

    def add(self, a, b):
        self.memory = a + b
        return self.memory

    def subtract(self, a, b):
        self.memory = a - b
        return self.memory
    
    def multiply(self, a, b):
        self.memory = a * b
        return self.memory

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        self.memory = a / b
        return self.memory

    def power(self, a, b):
        self.memory = a ** b
        return self.memory

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of a negative number!")
        self.memory = a ** 0.5
        return self.memory
    

