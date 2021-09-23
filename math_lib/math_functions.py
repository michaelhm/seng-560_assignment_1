from math import sqrt
from operator import add, sub, mul, truediv, pow

subtract = sub
multiply = mul
divide = truediv
exponent = pow
power = pow

def math_operations(x, operator, y=False):
    if (operator == sqrt):
        return sqrt(x)
    else:
        y = y if y else x
        return operator(x, y)