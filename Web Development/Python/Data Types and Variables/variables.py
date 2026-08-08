""" 
In this lesson I learnt about identifiers in python 
"""

# a variable is just a name or Identifier that helps to refer to an object in memory. e.g
my_name = 'habib'

# this identifier or name has some rules that it must conform with before it can be considered valid in python
# the first rule is that, the name can start with a Unicode character that is considered a letter or underscore and can be followed by zero or more continuation character
# the continuation character can be anything that is permitted as the start character, digits, and also case sensitive

# second rule, the name cannot be any of python keyword or any of python's builtin identifier
# to view this identifiers, we can use the dir() function which returns a list of attribute for an object. If passes with an empty argument, it returns a list of python attribute

print(dir())  # this returns the attributes that belongs to python and also the current file that we are in
print(dir(__builtins__))  # this returns the list of builtins attributes(methods and functions) in python

""" 
the third rule deals with the use of underscores in python. a single or double preceeding underscore without any trailing
underscore indicates a private methos or attribute, a single underscore on its own in the python shell evaluates to the
last evaluated value, while a name that starts and ends with double underscores are called speacial or dunder identifier
and this should not be reimplemented e.g __str__ 
"""
# examples of valid python identifiers, 
name = "Amot the Dev"
_other_name = "Amot"
name2 = "Amoto"
print("My names are ", name, _other_name, name2)

