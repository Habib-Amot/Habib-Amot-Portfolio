""" A module is just a python file that contains objects that is meant to used by other programs
    when a module is being imported, the module is being compiled by python and all the objects (classes, variables, functions and methods ) are being used as attributes of the the objects

    modules are imported in python using the import statement and this can be of different syntaxes depending on what we want to achieve
    here is how we can import anything in python
    import importable
    import importable, importable2, importable2 ... importableN
    import importable as name

    or we can import an object from a module or package
    from importable import object
    from importable.object import object
    from importable import object1, object2, object3 .. objectN
    from importable import *


    import are resolved by first looking at the source folder in which the executed file lives, then the sys.path folder is checked and then python path is checked

    In this lesson, we are going to create two custom modules, Textutil module and also Chargrid module

    A package is simply a directory that contains a set of modules and a file called __init__.py.

    below are examples that import objects and module from a package and module.
"""

from os import path  # imports the path function
from sys import path, platform  # imports two objects from sys
import time
import datetime
from datetime import timedelta

# let make use of our custom function from our module
from util_package.TextUtils import simplify

# and now we can start using the objects and modules that was imported


def show_current_time():
    print("the current time is {0}".format(datetime.datetime.now().time()))


show_current_time()

# we can use the time module and timedelta to create a function that executes after a minute

def shedule_task(task, minutes, *args, **kwargs):
    time_diff = timedelta(minutes=minutes)
    current_time = datetime.datetime.now()
    future_time = current_time + time_diff
    while True:
        if datetime.datetime.now() > future_time:
            task(*args, **kwargs)
            break
        else:
            time.sleep(2)
            continue


shedule_task(print, 0.05, "this is the first thing I want to print", "and this is the second thing that I want to print", sep="--", end="\n\n")

simplify(" Washington D.C.\n", delete=",;:.")
