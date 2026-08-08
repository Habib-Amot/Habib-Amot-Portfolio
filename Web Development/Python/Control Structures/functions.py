"""
Functions are a means by which we can package up and parameterize functionality.
A function is a way of organizing our code such they can be written without having to worry about writing the code every time we need them
"""

print("{0:=^40}".format("[CREATING FUNCTIONS]"))
# here is a function that display the list of my favorite places
def show_favorite_places():
    print("my favorite places: Mecca, Turkey and Cairo")
    
# functions can also be created to accept arguments in which there are two types: positional and keyword arguments

# here is a function that takes 3 names and prints out the longest of the names
def show_longest_name(name1, name2, name3):
    if len(name1) > len(name2) and len(name1) > len(name3):
        print(name1, "is the longest name")
    elif len(name2) > len(name3):
        print(name2, "Is the longest name")
    else:
        print(name3, "Is the longest name")


# creating a function is one thing, to make the code inside that function run, we need to call it
# calling a function is by putting parenthesis in front of the function name
# to call the show_longest_name function, we do
show_longest_name("habib", "Amoto", "Amot The Dev")

# Passing too much or too few arguments to a function causes an exception
try:
    show_longest_name("habib", "Amoto", "Gemini man", "Amot The Dev")
except TypeError:
    print("too much or too few arguments supplied")
    
# functions can also be created by passing default arguments to them as parameter
# here is a shorten function that has default indicator and length such that when they are not given, the default values are used
def shorten_text(text, length=10, indicator='...'):
    if len(text) > length:
        shorten_text = text[:length-len(indicator)] + indicator
        print(text, " is shorten to", shorten_text)
    else:
        print(text)


# now we can call the function with the text we want to shorten alone without having to worry about the indicator and length
shorten_text("Amot The Dev")

# default values should be taken with care, especially when they are mutable type
# this is because default values are created when a function is created. and if such value is not declared as private within the function,
# the default value will be used. This means all function calls use the same default value
# here is an example


def add_item(item, lst=[]):
    # lst = [] if lst is None else lst
    lst.append(item)
    print(lst)


# this will make the default list contain two items despite calling them differently
print("this are two function call but they access the same default list")
add_item(34)
add_item(56)

print()
print("Using Doctrings:")

# Doctrings are a way to add documentation to our function and giving instructions on how they can be used
# they are added after the def line and before the function code itself
# here is a different version of the show_longest_name function
def show_longest_name(name1, name2, name3):
    """ prints the Longest of three names
    
    each parameter must be a string and the printed valuebis also a string 
    
    >>>show_longest_name("habib1", "Amot", "Amoto")
    'habib1'
    """
    
    if len(name1) > len(name2) and len(name1) > len(name3):
        print(name1, "is the longest name")
    elif len(name2) > len(name3):
        print(name2, "Is the longest name")
    else:
        print(name3, "Is the longest name")

print()
print("{0:=^40}".format("[ARGUMENTS PACKING AND UNPACKING]"))
print("Packing and unpacking of arguments can be done with * and **")
# when we have the * or ** at the left of an assigment operator, it is used as Packing
# when present at the front of an iterable, it is used as unpacking
# this functionality can be used in function arguments as well
print()
print("Parking positional args:")
def multiply_number(*args):  # all positional arguments will be packed as a list and stored in args
    result = 1
    for num in args:
        result *= num
    print("multiplication of {} is {}".format(args, result))


multiply_number(1, 3, 4, 50)
# we can store this data in a list and unpack the items of the list inside our function
print()
print("Upacking positional args")
numbers = [10, 10, 32, 100]
multiply_number(*numbers)  # this will be called with all elements of numbers and then packed again as args

print()
print("Packing keyword args")
# Packing keyword args is done with ** and it takes all keyword args and convert them to dict


def show_details(ssn, username, **kwargs):  # **kwargs means take all keyword args, put them in a dict and store it in kwargs
    print("SSN: {}".format(ssn))
    print("    Username: {}".format(username))
    for key in kwargs:
        print("    {}: {}".format(key, kwargs[key]))


show_details("123-568-amt456", "Amot The Dev", age=45, classname="first class", profession="Programming")
# and we can now pass ssn and username via dictionary unpacking

print()
print("Unpacking keyword args:")
details = {
    "age":32,
    "dob":2001,
    "dept":"Computer science",
    "class":"first class"
}
show_details("123-568-amt456", "Amot The Dev", **details)


# This means that we can create function that accepts both keyword args and positional args
# and we can create a function that accept just either of them or none of them


def receive_no_pos(*, func_type="No Positional Arguments type"):
    print("This is a {} of function".format(func_type))
    

print()
try:
    print("Calling receive_no_pos with a Positional arg")
    receive_no_pos(12, 34)
except TypeError:
    print("receive_no_pos accepts no positional arg")
    
print()
print("{0:=^40}".format("[LAMBDA FUNCTIONS]"))
print("lambda functions are anonymous functions that are created by python itself")
# they take optional positional args and cannot have loops, yield kr return statement
# e.g
area = lambda h, b: 0.5 * h * b
height = 12
base = 10
triangle_area = area(height, base)
print("The area of a triangle with height {} and base {} is {}".format(height, base, triangle_area))
