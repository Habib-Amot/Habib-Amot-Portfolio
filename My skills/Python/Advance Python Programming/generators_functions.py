import os
import sys
import glob

""" Generators are methods that returns their items one at a time.
    that can be called lazy evaluation funtions that only return the values is necessary at a particular point in time
"""

# there are two ways in which a generator can be created in python
# using the yield keyword or by making use of generator expressions

# using the yield keyword

def get_names():
    my_names = ['habib', 'Amot', 'Amot the dev']
    for name in my_names:
        yield name  # this will cause a name to be returned at a time

for name in get_names():  
    print(name)  


# this function return one number at a time, and then when called again, it returns the next number
def get_quater(start=0.0):
    while True:
        yield start
        start  += 0.5

for value in get_quater():
    print(value)
    if value > 20: break  # this is important, as the get_quater function will keep running if we did not call break

# here is an example that yield the names of files given on the command line and also supports globbing
# each file is returned one at a time using the yield keyword


if sys.platform.startswith('win'):
    def get_files(filenames):
        for file in filenames:
            if os.path.isfile(file):
                yield file
            else:
                more_files = glob.iglob(file)
                for file in more_files:
                    if not os.path.isfile(file):
                        continue
                    yield file
else:
    def get_files(filenames):
        return (file for file in filenames if os.path.isfile(file))  # using the expression generator syntax

files = []
for file in get_files(sys.argv[1:]):
    print(file)
    if len(files) > 2:
        break
    else:
        files.append(file)
