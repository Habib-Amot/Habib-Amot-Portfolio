import doctest
import unittest

# Testing is a very important and beneficial aspect of programming that helps to ensure and ascertain that our code and program is functioning as it should
# when done very well, tests helps to spot problems before they escalate or become bugs that might be difficult to trace later
# this is why it is often very helpful to test components as they are being built

# The basic units of test are functions, and to better write tests, it is always a best practice to test the input and then check the output for the desired and
# expected outcome
# Test are done in Four  steps:
# 1. Setup the Test fixtures
# 2. Create the Test Case(s)
# 3. Create a test suite
# 4. Run the test

# say there is a function that takes two number as it's input and the want to test it, this can be done like

def add_number(x: int, y: int):
    """
    Docstring for add_number
    
    :param x: The first number that is to be added
    :type x: int
    :param y: The second number that is to be added
    :type y: int

    >>> add_number(4, 5)
    9
    >>> add_number(4, 0)
    4
    >>> add_number(10, 'habib')
    File "<python-input-0>", line 1, in <module>
    4 + 'habib'
    ~~^~~~~~~~~
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x + y


# and now, a doctest can be performed on the function
if __name__ == "__main__":
    doctest.testmod()

