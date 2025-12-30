""" In python, there are two main integral types -> Integer and Booleans 
    Integers are mainly any non-floating point value 
    and most mathematical operations can be performed with them.
    Booleans are treated like integers when used in the context of integers with True evaluating to 1 and False evaluating to 0

"""

number_of_oranges = 10
number_of_mangoes = 10
total_number_of_fruits = number_of_oranges + number_of_mangoes
print(total_number_of_fruits)  # prints 20

# integers supports many mathematical operators like: +, -, *, **, /, //, %
# there are also builtin functions that is used to work with integers, e.g round, pow
print(total_number_of_fruits % 3)  # divides number of fruits by 3 and returns the remainder
print(divmod(total_number_of_fruits, 3))  # returns the integer part and remainder in tuple of dviding number of fruits by 3
print(round(1505.554, 1)) # rounds the given number to one decimal place
print(round(1507, -1)) # providing a negative value to round, will round the given number to nearest number given

# any integer can also be converted to and from binary, hexadecimal and octal value using bin, hex, and oct respectively
print(bin(number_of_mangoes), hex(number_of_mangoes), oct(number_of_mangoes))

# or they can be written in their literal form and will be evaluated to decimal at runtime e.g
ten_in_hex = 0xa  # in hexadecimal
ten_in_oct = 0o12  # in octal
ten_in_binary = 0b1010  # binary value
print(ten_in_binary, ten_in_hex, ten_in_oct)  # each will be evaluated to 10
# the int function can be used to convert a given string value that is in a particular base to its integer form by passing
# the string representation of that number and also the base
print(int("0b1010", 2))

""" Integer type can be created using one of two methods -  using the literal or using the data type method of int """
# while using the data type, values can be created by not passing any value at all - return 0
# or providing a single value: if this value is an int, a shallow copy is returned, else a conversion is attempted
# if the conversion fails and the type supports conversion to the type, a ValueError is raised. If the type does not,
# a TypeError is raised e.g
print(int())  # prints 0
print(int(10))  # return the shallow copy of 10
print(int('35'))  # return the literal 35
try:
    print(int('please'))  # returns a ValueError
except ValueError:
    print("value cannot be converted to integer")
print(int(12.5))  # return 12
try:
    print(int([1, 3]))  # returns a TypeError
except TypeError:
    print("value does not support integer conversion")

# bitwise operators operates on the bit of a particular integer e.g and returns the result as an int e.g
print("the bitwise value of 20 OR 10 is ", 20 | 10)  # perform OR operation on 10100 and 01010 --> 11110
print("the bitwise value of 20 XOR 16 is ", 20 ^ 16)  # perform XOR operation on 10100 and 01010 --> 00100
print("the bitwise value of 20 AND 10 is ", 20 & 10)  # perform AND operation on 10100 and 01010 --> 00000
# we can invert the result by flipping the bits
print("the bitwise value of NOT(20 AND 10) is ", ~(20 & 10))  # flips 00000 --> 11111

""" Booleans are treated like number True = 1, False = 0 """
print(True + False) # 1
print(True + True)  # 2
print(False + False) # 0

