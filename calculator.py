"""A small calculator class used to demonstrate unit testing and code coverage."""

import math

class Calculator:
    """Basic calculator supporting the common arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


    def divide(self, a, b):
        # dividing by zero would crash with a confusing error, so we raise our own
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        return base ** exponent

    
    def square_root(self, value):
        # negative numbers have no real square root, so we stop early
        if value < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(value)

      
    def power(self, base, exponent):
        return base ** exponent
