from collections import namedtuple
import math
from utils import show_heading

""" In this lesson, we are going to talk about list and tuples collection data types
"""


show_heading("[TUPLE DATA TYPE]")
""" A tuple is an ordered sequence of zero or more object references.
"""
# tuples are creatwed using commas, or using the tuple function
# tuples can be optionally wrapped with parenthesis e.g
print("Creating Tuples:")
hair = "black", "blonde", "brown", "red"
print("common hair types", hair)

# tuples can appear at the left side of an assignment operator or the right side of ite
# when they appear at the left side, it is best to ommit the parenthesis, and when they appear at the right side they should be used
# e.g
name, age = ("habib", 30)
# can also be written as 
name2, age2 = "habib", 30
print(name, name2, age2, age)

# just like strings tuples are immutable and also suports slicing and striding
# and also membership testing using in and not in e.g
print()
print("Slicing tuples:")
print("here is a sliced hair", hair[1:2])

# Each items in a tuple can be given a name to reference it, which makes tuples really cool
# to name each items in a tuple, we make use of namedtuples
print()
print("Using namedtuple:")
aircraft_details = namedtuple("AircraftDetail", "seat_number name manufacturer")
aircraft1 = aircraft_details(154, "Boeing 500", "Boeing")
print("aircraft1 name is ",aircraft1.name)
# and the namedtuple object can be converted to dictionary
print(aircraft1._asdict())

print()
show_heading("[LIST DATA TYPE]")
""" List are collections of items that are identifies for the items they store. They can indexed, sliced and strided and just like strings, they
    support membership in and not in operator
    e.g
"""
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = [11, 12, 13, 14, 15]
print(f'Using the List {L} and\nList {L2}')
print('slicing and striding:')
print('this is a sliced list item', L[1:8])
print('this is a strided list item', L[::-1])  # this will cause the list to be reversed
# we can using slicing or striding to replace items at certain positions
L[1::2] = [1] * len(L[1::2])
print('replacing every item at an even position with 0', )
print()
print("Packing and Unpacking of iterables:")
# the * and ** operator is are used for packing and unpacking of items in an collection
# when the * or ** operator is used in front of a collection item and not in a binary operation, they are used for unpacking
# while when they are used in a keyword or positional argument, they are used for packing. e.g
first, *mid, last = L  # in this case, first will hold the first item in the list L and mid will hold the remaining item aside the last one which is for last
print(f"this is the first: {first}\nand these are the middle items:{mid}\nwhile this is the last item:{last}")
# the print function receives arbitrary number of positional arguments and we can pass this arguments to it without having to loop over each item
print("these area all unpacked from the list L", *L)  # this will cause L to be unpacked and passed to the print function
print()
print("List methods:")
# list can be combined together using either the + operator, or the extend method. e.g
L.extend(L2)
print("extending L with L2", L)  # same as L+=L2
# list can also be sorted or reversed. while sorting, we can pass in the key that will be used during the sorting operation
# for example we can sort our list based on the square root of each of them
L.sort(key=lambda a: math.cbrt(a)/a)
print("this is a sorted List, but the sorting is done by taking the cube root of each number and dividing it by the number: ", L)
# removing the last item in the list
L.pop()
print()
print("Using range:")
# the range function allow for creating an iterable that contains numbers usually from the start to the end of the argument passed to range
# e.g
one_to_10 = range(1, 11)  # returns an iterable that can be looped over and produces number 1 to 10
# using step
even_numbers = range(0, 11, 2)  # returns an iterable that contains all even numbers between 0 and 10
print()
print("List comprehension:")
# list comprehension is a way of generating list items using a one liner. 
# using the range items from above, we can use list comprehension to create the list items
one_to_10 = [number for number in one_to_10]  # create list of numbers from 1 to 10
even_numbers = [even_number for even_number in even_numbers]  # create list of even numbers from 1 to 10
print("This are created using the range funtion: {0}, {1}".format(one_to_10, even_numbers))
