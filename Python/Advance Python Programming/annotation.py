import os
import inspect
import functools

# annotations in python are a means of making codes more readable and explainable to other devs
# it adds clarity to codes and makes it more understandable 
# but these annotations are not evaluated by python or has any other meaning aside that they are store in a function __annotations__ property

# here is an annotated function
def is_csv(filename: str) -> bool:
    file_name, file_ext = os.path.splitext(filename)
    return file_ext == ".csv"

file = "customer_names.csv"
print(f"checking if {file} is a csv file not....")
print(f"{file} is {'a' if is_csv(file) else 'not a'} csv file")

# and the annotations of the function can be checked as well
print("is_csv function annotations -> ", is_csv.__annotations__)

# and by making use of annotations, it is possible to create a function that is strictly typed
def strictly_typed(function):
    function_annotations = function.__annotations__
    function_args_spec = inspect.getfullargspec(function)
    # 1. making sure the function returns a value
    assert 'return' in function_annotations, f"{function.__name__} failed to return a value"

    # 2. making sure all the function args and kwargs are all annotated
    for arg in list(function_args_spec.args) + list(function_args_spec.kwonlyargs):
        assert arg in function_annotations, f"type of {arg} not known"
    
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result
    
    return wrapper


# and now the decorator can be used
@strictly_typed
def is_not_csv(filename):  # will cause assertion error because thr functuon does not have a return annotation
    file_name, file_ext = os.path.splitext(filename)
    return file_ext != ".csv"


