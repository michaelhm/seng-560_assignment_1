from math_lib import math_functions

func = math_functions.MundyCalc

def test_setValue():
    result = func.setValue(3, None)
    assert result == 3

def test_add():
    testInteger = func.add(2, 3)
    testFloating = func.add(2.5, 2.5)
    testBinary = func.add(0b10, 0b11)
    testHexadecimal = func.add(0x02, 0x03)
    testOctal = func.add(0o02, 0o03)
    testSelf = func.add(2)
    assert (testInteger, testFloating, testBinary, testHexadecimal, testOctal, testSelf) == (5, 5, 5, 5, 5, 4)

def test_subtract():
    testInteger = func.subtract(3, 2)
    testFloating = func.subtract(3.5, 2.5)
    testBinary = func.subtract(0b11, 0b10)
    testHexadecimal = func.subtract(0x03, 0x02)
    testOctal = func.subtract(0o03, 0o02)
    testSelf = func.subtract(2)
    assert (testInteger, testFloating, testBinary, testHexadecimal, testOctal, testSelf) == (1, 1, 1, 1, 1, 0)

def test_divide():
    testInteger = func.divide(6, 3)
    testFloating = func.divide(4.4, 2.2)
    testBinary = func.divide(0b110, 0b11)
    testHexadecimal = func.divide(0x06, 0x03)
    testOctal = func.divide(0o06, 0o03)
    testSelf = func.divide(2)
    assert (testInteger, testFloating, testBinary, testHexadecimal, testOctal, testSelf) == (2, 2, 2, 2, 2, 1)

def test_multiply():
    testInteger = func.multiply(2, 3)
    testFloating = func.multiply(2.5, 2.4)
    testBinary =  func.multiply(0b10, 0b11)
    testHexadecimal = func.multiply(0x02, 0x03)
    testOctal = func.multiply(0o03, 0o02)
    testSelf = func.multiply(2)
    assert (testInteger, testFloating, testBinary, testHexadecimal, testOctal, testSelf) ==(6, 6, 6, 6, 6, 4)

def test_exponent():
    testInteger = func.power(2, 3)
    testFloating = func.power(2.5, 2)
    testBinary = func.power(0b10, 0b11)
    testHexadecimal = func.power(0x02, 0x03)
    testOctal = func.power(0o02, 0o03)
    testSelf = func.power(2)
    assert (testInteger, testFloating, testBinary, testHexadecimal, testOctal, testSelf) == (8, 6.25, 8, 8, 8, 4)

def test_sqrt():
    testInteger = func.sqrt(4)
    testFloating = func.sqrt(4.5)
    testBinary = func.sqrt(0b100)
    testHexadecimal = func.sqrt(0x04)
    testOctal = func.sqrt(0o04)
    assert (testInteger, round(testFloating, 2), testBinary, testHexadecimal, testOctal) == (2, 2.12, 2, 2, 2)