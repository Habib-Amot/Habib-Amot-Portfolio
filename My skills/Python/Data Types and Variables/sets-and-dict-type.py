import string
from collections import defaultdict
import copy

from utils import show_heading

""" This lesson is for Dictionary and Sets in python """

show_heading("[SET DATA TYPE]")
"""
A set type is a collection data type that supports the membership operator (in),the size function (len()), and is iterable.
A set only stores hashable data types. This is because it uses their hash value to referece them. This means that only hashble types (str, int, 
bool, frozensets, floats and tuples) can be stored in them.
Sets are unorderd, so they do not support indexing
"""
S = {21, "Amot", 43.21, True, (21, 54), 100, 34}  # set of items
S2 = {21, 34, 67, 34, 90, 100, 105, 399}
print("Using the Set:", S, " and ", S2)
union_set = S | S2  # combine set S and S2
intersection_set = S & S2  # get what is common between set S and S2
difference_set = S - S2  # remove the common items from set S
print("the union of S and S2 is: ", union_set)
print("Intersection of set S and S2: ", intersection_set)
print("Difference of set S and S2: ", difference_set)
print()
print("Set Comprehension:")
# set can also be created using one liner method to create them
# let say we want to create a set of numbers that are divisible by 3 from 1 - 100 using set comprehension, we can say
multiple_of_3 = {number for number in range(1, 101) if number % 3 == 0}
print("these multiples of three are created using set comprehension:\n", multiple_of_3,sep="")
print()
print("Frozen Sets:")
# frozen sets are sets that are immutable i.e cannot be changes once they are created. they are created using the frozenset function
frozen_names = frozenset({'habib', "amoto", 'erudite'})
print("this names are frozen and cannot be change", frozen_names)
print()
show_heading("[DICTIONARIES (dict, defaultdict, OrderedDict)]")
# dictionaries can be created using several ways either throught the literal form, or passing an iterable of iterables to the dict function,
# or passing literal dict to the dict function, or calling the dict function (which returns an empty dictionary), passing keyword args to dict
# focus will be on few of these methods
d = {"root": 18, "blue": [75, "R", 2], 21: "venus", -14: None, "mars": "rover", (4, 11): 18, 0: 45}
print("Using the dictionary: ", d)
print()
print("Dictionary Views:")
# dictionary views are effectively read-only and are gotten when we call .keys(), .items() or .values() method of a dictionary. # an attempt to write to these views will cause an error
print("this is the key view of the d dictionary: ", d.keys())
print("this is the values view of the d dictionary: ", d.values())
print("this is the items view of the d dictionary: ", d.items())

# a dictionary contains unique items, so we can use this feature to store values that are unique. 
# for example, the function below gets every word in a file and store their counts without repetition of words.


def count_unique_word_in_file(filename:str) -> None:
    words = {}  # holds the each unique word in the file
    strips = string.punctuation + string.digits + string.whitespace + "'\""
    try:
        for line in open(filename):
            word_list = line.split()  # splitting the lines with spaces
            for word in word_list:
                word = word.lower().strip(strips)
                if len(word) > 2:  # making sure what we have is a word and not just a single character
                    words[word] = words.get(word, 0) + 1  # incrementing the count of the word
        # printing out the word counts
        if len(words) > 0:
            print(f"The word count from {filename} is {words}")
    except FileNotFoundError, OSError:
        print('unable to find file {}'.format(filename))


print()
print("Dictionary Comprehension:")
# dictionaries can also be created using dictionary comprehension
# say we want to create unique names and their lenght
name_length = {name:len(name) for name in ["chipper stonezy", 'Amot the Dev', "The real amot"]}
print(f"this name info is created using dictionary comprehension {name_length}")

print()
show_heading("[DEFAULT DICTIONARY]")
# a default dictionary is a type that has a default value for items that are not present inside our dictionary. This function takes a factory
# function which will be called when an item is not found inside the dictionary
# using our name lenght example
uppercase_letter = defaultdict(int)
# now when we try to get an item from the dictionary and it is not available, that dictionary will run the factory funtion and return the item returned by it
uppercase_letter.update({}.fromkeys(string.ascii_uppercase, 1))
print("this is the deafault value when a key is not found in the dict", uppercase_letter['q'])
print()
show_heading("[ITERATORS AND ITERABLES]")
# an iterable is an object (sequence, collection type) that either has a __getitem__() method or can return an iterator object through its __iter__() method
# the iterator object has a __next__() method which is called subsequently till a StopIteration error is raise
# here is an example that mimicks python for loop
print("Mimicking python for loop (this is printed using the iterator inteface)")
iterator = iter(d)  # this calls the __iter__() method of d and it returns iterator object
while True:
    try:
        next_item = next(iterator)  # this calls the __next__() method of the iterator
        print(next_item)
    except StopIteration:
        break

print()
show_heading("[MORE COLLECTION FUNCTIONS]")
# more functions for collection types
# checking if all items inside a collection is true, that is it does not contain any false vale
print(f"every value inside {S} is {'' if all(S) else 'not'} true")
# now let's add a falsy value inside this set
S.add(0)
print(f"every value inside {S} is {'' if all(S) else 'not'} true")
# checking if any value is true
print(f"some value inside {S} is {'' if any(S) else 'not'} true")
# getting lenght, max and min value and sum of a collection
print(f"the length of S2 is {len(S2)} and the maximum value is {max(S2)} while the minimum value is {min(S2)}\ntotal sum: {sum(S2)}")
print()
print("Sorting and Reversing items:")
names = ['Amoto', 'amoto', 'Habib', "Aisha", 'habib', "Zainab"]
favorite_numbers = [5, 6, 55, 66, 10, 11, 98, 0, 1, -5, -7, 9]
print(f"sorted names case-sensitively:".format(sorted(names)))
print(f"sorted names case-insensitively:".format(sorted(names, key=str.lower)))  # the key arguments allow us to pass a function about how we want to sort our items
# using the reverse method
print("reversed of {0}: {1}".format(favorite_numbers, list(reversed(favorite_numbers))))
print("sort of {0}: {1}".format(favorite_numbers, sorted(favorite_numbers)))
print("sorting  of {0} without considering signs: {1}".format(favorite_numbers, sorted(favorite_numbers, key=abs)))

print()
show_heading("[COPYING COLLECTSION (shallow and deep copying)]")
# when two objects reference refer to the same object and the object is mutable, it means they both have access to the same object and any changes
# made by either of the objects references will reflect in both ways e.g
my_names = names
print('first collection ', names)
print('second collection', my_names)
print()
# lets make a change via the my_names object reference
my_names[0] = "Amot"
print('changes is made in second collection but it affects the second collection')  # this is because they both refer to the same object
print('first collection ', names)
print('second collection', my_names)
print()
print("Shallow copying:")
# shallow copying happens when an object reference points to an object and another object reference copies part or the entire object being referred to
favorite_food = ['rice', 'beans', 'garri', 'yam', ['semo', 'eba', 'pounded yam']]  # original copy
my_favorite_food = favorite_food[:3]

# despite the fact that my_favorite_food copied from favorite_food, changing items in either object reference will not affect neiter of them
# this is due to the way collections are stored. Collections store their items as objects reference then items are bind to the object reference
# modifying either of the collection will not affect each other because the items copied are immutable
my_favorite_food[0] = 'cocoa yam'
print(favorite_food)
print(my_favorite_food)

all_my_favorite_food = favorite_food[:]  # now the collection inside favorite_food  objects reference is also copied
print('changing the list of swallow via all_my_favorite_food object reference')
all_my_favorite_food[4][0] = "cocoa yam"
favorite_food[4][1] = "spagetti"
print(all_my_favorite_food)   
print(favorite_food)  

# to make a copy of these items in-depth, we need to make use of deep copying
print()
print("Deep copying:")
all_my_favorite_food = copy.deepcopy(favorite_food)
# now changing values in either objects reference will not affect neither of them
all_my_favorite_food[4][1] = 'potatoe'
print("one list one will be affected now ")
print(all_my_favorite_food)   
print(favorite_food)  
