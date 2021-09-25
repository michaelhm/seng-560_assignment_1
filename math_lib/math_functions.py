from math import sqrt
from operator import add, sub, mul, truediv, pow
from typing import Any

class MundyMath:
    def setValue(x, y):
        return x if y is None else y

    def add(x, y = None):
        y = MundyMath.setValue(x, y)
        return add(x, y)

    def subtract(x, y = None):
        y = MundyMath.setValue(x, y)
        return sub(x, y)
    
    def multiply(x, y = None):
        y = MundyMath.setValue(x, y)
        return mul(x, y)

    def divide(x, y = None):
        y = MundyMath.setValue(x, y)
        if (y == 0):
            result = print('Divide by zero error')
        else:
            result = truediv(x, y)
        return result

    def power(x, y = None):
        y = MundyMath.setValue(x, y)
        return pow(x, y)

    def sqrt(x):
        return sqrt(x)