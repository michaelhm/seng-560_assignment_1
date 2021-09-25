# seng-560_assignment_1

## MundyCalc

This is a Python library which is capable of performing the following math evaluations:
* add
* subtract
* multiply
* divide
* power
* square root

## How to Use
### Preferred method:
#### Pipenv
[Pipenv](https://pipenv.pypa.io/en/latest/) is a tool for managing packages. It combines Pipfile, pip, and virtualenv into a single tool.

**Install** `pipenv`:  
`pip install --user pipenv`

**Run:**  
`pipenv shell` This starts a shell within the virtualenv

**Run:**  
`pipenv install --dev` This installs all dependencies including dev

**Run:**  
`python setup.py bdist_wheel` This creates a dist folder with a wheel file

**Run:**  
`pipenv install /path/to/wheelfile.whl/` This installs the library

Now the library can be imported for use:  
`import from math_lib import math_functions`

### Alternative method:x
If you prefer not to use a virtual environment, install dependencies, or build and install the library then you can simply import the library as long as it is in your project folder structure:  
`import from math_lib import math_functions`

### Performing function calls:
Assign `math_functions.MundyCalc` class to a variable for easier use  

**Example:**  
    `func = math_functions.MundyCalc`  
    `print(func.add(3, 4))`  
    `Output: 7`

add (`add()`), subtract (`subtract()`), multiply (`multiply()`), divide (`divide()`), and power (`power()`) functions each accept two arguments `x, y`  
y is an optional argument.
If only a value for x is passed, then the function will use x's value for y to perform the operation on "itself."  

**Example:**  
    `add(3)` will evaluate to **6** `(3 + 3)`.  
    This is to replicate the functionality of a calculator if one was to enter `3 + =`  
    Try it on your phone's calculator :)

Divide function performs a check for divide by zero and displays an appropriate message to the user

Square root (`sqrt()`) accepts a single argument `x` to perform its calculation

Conversion between the various types (octal, hexadecimal, integer, binary) is supported.

**Binary Example**  
    `add(0b10, 0b11)` evaluates to `5`

## Unit Tests
The library has 100% code coverage (7 tests for 7 functions)  
Each of the 6 math functions test the following types, conversions, and final evaluations:
* Integer
* Floating
* Binary
* Hexadecimal
* Octal

Unit tests are located in `/tests/` and can be run by issuing command `pytest` at the library root folder  
    **This can command can only be run if `pipenv` and library dependencies have been installed**  

All types must convert and evaluate correctly or else the test will fail:
> ============ test session starts ===============  
> platform linux -- Python 3.9.5, pytest-6.2.5, py-1.10.0, pluggy-1.0.0  
> rootdir: seng-560_assignment1  
> collected 7 items  
> tests/test_functions.py ....... [100%]  
> ============ 7 passed in 0.07s =================

## Reusability
All 6 math functions are reusable for all number types outlined in the requirements  
The use of `pipenv` expands reuse as a package manager (installing dependencies) and enabling the use of a virtual environment  
The virtual environment ensures compatibility by installing the library's required Python version, along with any additional packages, for use