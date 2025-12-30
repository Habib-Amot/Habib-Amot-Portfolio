import math
from decimal import Decimal
""" This lesson is about floating points numbers --> floats, decimal.Decimal, and complex number """

# floating point numbers can be written in python using the literal form or the exponential form e.g
price_of_fuel = 45.34
epsilon = 0.1e-10
print(epsilon)
print(epsilon.as_integer_ratio())  # this provides the integer part and also the divisor
# also fractions can be expressed in hex format 
print(price_of_fuel.hex())  # returns the hex value of price_of_fuel
print(float.fromhex('0x1.ffffp10'))  # coverts this hex number back to its floating form

""" Complex Numbers """
# complex number are also floating point numbers that consists of two parts, the real and the imaginary part
# the literal form of it are
c = 2.5+1j 
# this literal can be used with some methods to find the real and the imaginary part of it
print(f'the real part of {c} is {c.real} and the imaginary part is {c.imag}')

""" Decimal Numbers """
# Decimal data types are like floats but except with the fact that they provide more accuracy and precision compared to floats
# this makes Decimal data types to be slower compared to floats. They cannot be represented using literals but can be created
# using the Decimal class for example
bank_balance = Decimal(23) / Decimal("1.023")
float_bank_balance = 23 / 1.023
# from this two prints below, we can see that floats has low accuracy compared to Decimal numbers 
print(bank_balance)  # more accuracy
print(float_bank_balance)  # lesser accuracy

# lets create a simple bank account that allows users to add and remove money and also finds the average amount of expenses
account_balance = 3000.5
price_of_orange = 10.11
price_of_rice = 100.99
price_of_banana = 20.123
total_expenses = price_of_orange + price_of_banana + price_of_rice
balance_left = account_balance - total_expenses

# for better accuracy, lets convert this floating point number to Decimal
total_expenses = Decimal.from_float(total_expenses)
print(f"the average amount of expenses is ${total_expenses / 3} and amount left is ${balance_left}")
