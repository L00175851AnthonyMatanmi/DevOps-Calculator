"""A small calculator class used to demonstrate unit testing and code coverage."""


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
