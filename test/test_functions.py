from math_lib import functions
from operator import add, sub, mul, truediv, pow
from math import sqrt

def test_math_operations_add():
    assert functions.math_operations(3, add, 4) == 7

def test_math_operations_subtract():
    assert functions.math_operations(4, sub, 3) == 1

def test_math_operations_divide():
    assert functions.math_operations(6, truediv, 3) == 2

def test_math_operations_multiply():
    assert functions.math_operations(2, mul, 3) == 6

def test_math_operations_exponent():
    assert functions.math_operations(2, pow, 3) == 8

def test_math_operations_sqrt():
    assert functions.math_operations(4, sqrt) == 2