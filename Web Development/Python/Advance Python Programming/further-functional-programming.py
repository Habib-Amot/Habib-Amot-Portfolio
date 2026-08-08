# this lesson involves mapping, filtering, and reducing iterables using the map, filter and reduce function
import os.path
import random
import pathlib
import operator
import functools

print("{0:=^50}".format("[MAPPING]"))
# first, we talk about mapping.
# mapping is the way of taking a function and also an iterable and then passing each of the item in the iterable to the
# provided function which in turn returns a new iterable of the applied functin

student_score = [23, 45, 67, 39, 10]  # say there are 5 student in a class, and we want to increase their scores by 10
print("initial scores of student", student_score)
# this can be achieved by using the map built-in method

new_student_score = map(lambda a: a + 10, student_score)  # returns a map object
print("new student score after increasing it", list(new_student_score))

print("\n{0:=^50}".format("[FILTERING]"))
# filtering is the process of taking an iterable and passing it to a function to see if it passes the test or not
# this is implemented using the filter funtion

# here is a test sample data that is created randomly for the sake of practice
ages_in_futa = [random.randint(10, 35) for _ in range(101)]
print("ages of student in FUTA: ", ages_in_futa)

# say we want to remove students age who are below from the list
qualified_student = filter(lambda a: a >= 18, ages_in_futa)
print("Qualified Students: ", list(qualified_student))

# another function to consider is the reduce function which acts as a summarizer
# say there are some items in a cart and I want to get the total price of the items in the cart, reduce can be used here
print("\n{0:=^50}".format("[REDUCING]"))
prices_of_items_in_cart = random.sample(range(200, 1000), 10)
print("prices_of_items_in_cart".replace("_", " "), prices_of_items_in_cart)

# getting the total sum of the prices
total = functools.reduce(lambda a, b: a + b, prices_of_items_in_cart)
print(f"the total price of items bought is ${total}")

# another practical example of using this functional style of programming is getting the total file size in a folder
# say you want to get the total size of python files in this file current directory, this can be achieved in a line
file_path = pathlib.Path(__file__).parent
total_file_size = functools.reduce(operator.add,
                                   map(lambda file: os.path.getsize(file),
                                       filter(lambda a: a.endswith('.py'), os.listdir(file_path))
                                       )
                                   )
print(f"the total size of python files in {file_path} is {total_file_size: ,} bytes")
