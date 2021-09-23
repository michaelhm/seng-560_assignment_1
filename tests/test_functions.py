from math_lib import math_functions
from operator import add, sub, mul, truediv, pow
from math import sqrt

math_func = math_functions.math_operations

def test_math_operations_add():
    testInteger = math_func(2, add, 3)
    testBinary = math_func(0b10, add, 0b11)
    testHexadecimal = math_func(0x02, add, 0x03)
    testOctal = math_func(0o02, add, 0o03)
    testSelf = math_func(2, add)
    assert (testInteger, testBinary, testHexadecimal, testOctal, testSelf) == (5, 5, 5, 5, 4)

def test_math_operations_subtract():
    testInteger = math_func(3, sub, 2)
    testBinary = math_func(0b11, sub, 0b10)
    testHexadecimal = math_func(0x03, sub, 0x02)
    testOctal = math_func(0o03, sub, 0o02)
    testSelf = math_func(2, sub)
    assert (testInteger, testBinary, testHexadecimal, testOctal, testSelf) == (1, 1, 1, 1, 0)

def test_math_operations_divide():
    testInteger = math_func(6, truediv, 3)
    testBinary = math_func(0b110, truediv, 0b11)
    testHexadecimal = math_func(0x06, truediv, 0x03)
    testOctal = math_func(0o06, truediv, 0o03)
    testSelf = math_func(2, truediv)
    assert (testInteger, testBinary, testHexadecimal, testOctal, testSelf) == (2, 2, 2, 2, 1)

def test_math_operations_multiply():
    testInteger = math_func(2, mul, 3)
    testBinary =  math_func(0b10, mul, 0b11)
    testHexadecimal = math_func(0x02, mul, 0x03)
    testOctal = math_func(0o03, mul, 0o02)
    testSelf = math_func(2, mul)
    assert (testInteger, testBinary, testHexadecimal, testOctal, testSelf) ==(6, 6, 6, 6, 4)

def test_math_operations_exponent():
    testInteger = math_func(2, pow, 3)
    testBinary = math_func(0b10, pow, 0b11)
    testHexadecimal = math_func(0x02, pow, 0x03)
    testOctal = math_func(0o02, pow, 0o03)
    testSelf = math_func(2, pow)
    assert (testInteger, testBinary, testHexadecimal, testOctal, testSelf) == (8, 8, 8, 8, 4)

def test_math_operations_sqrt():
    testInteger = math_func(4, sqrt)
    testBinary = math_func(0b100, sqrt)
    testHexadecimal = math_func(0x04, sqrt)
    testOctal = math_func(0o04, sqrt)
    assert (testInteger, testBinary, testHexadecimal, testOctal) == (2, 2, 2, 2)