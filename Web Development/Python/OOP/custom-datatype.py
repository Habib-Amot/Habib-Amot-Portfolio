""" Creating custom data types involves building data types that can be inherited from or used to create instances that can used in our code
    When creating custom data types, we are left with two options, first is to create the object from scratch (although the object will still inherit from object) 
    and the second way is to create the data types from an existing data types
"""

# creating a data type from scratch
import pickle
from types import UnionType
from typing import Any


class FuzzyBool:
    def __init__(self, value: float=0.0) -> None:
        # encapsulating the value attribute and making sure only value 0.0 and 1.0 are allowed
        self.__value = value if 0.0 <= value <= 1.0 else 0.0 
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        raise AttributeError
    

    def __invert__(self):  # ~FuzzyBool(1.0)
        return FuzzyBool(1.0 - self.__value)
    
    def __bool__(self):  # bool(0.2)
        return self.__value >= 0.5
    
    def __format__(self, format_spec: str) -> str:
        return self.__value.__format__(format_spec)
    
    def __str__(self) -> str:
        return str(self.__value)
    
    def __repr__(self) -> str:
        return "{0}({1})".format(self.__class__.__name__, self.__value)
    
    def __and__(self, other):
        return FuzzyBool(self.__value) if not FuzzyBool(self.__value) else other
    
    def __or__(self: FuzzyBool, other: Any) -> Any:
        return FuzzyBool(self.__value) if FuzzyBool(self.__value) else other
    
    def __lt__(self, other):
        assert isinstance(other, FuzzyBool), "unsupported operation with type {0}".format(other.__class__.__name__)
        return self.__value < other.__value
    
    def __le__(self, other):
        assert isinstance(other, FuzzyBool), "unsupported operation with type {0}".format(other.__class__.__name__)
        return self.__value <= other.__value
    
    def __eq__(self, other) -> bool:
        assert isinstance(other, FuzzyBool), "unsupported operation with type {0}".format(other.__class__.__name__)
        return self.__value == other.__value
    
    def __hash__(self) -> int:
        return hash(id(self))
    

print("{0:=^40}".format("[CREATING DATATYPES FROM SCRATCH]"))    
print("created two instances of the FuzzyBool class")
test = FuzzyBool(1.0)
test2 = FuzzyBool(0)
print("FuzzyBool(1.0) & FuzzyBool(0) = ", test2 & test)
print("FuzzyBool(1.0) | FuzzyBool(0) = ", test2 | test )
print("FuzzyBool(1.0) == FuzzyBool(0) = ", test == test2)
print("FuzzyBool(1.0) <= FuzzyBool(0) = ", test <= test2)
print("FuzzyBool(1.0) >= FuzzyBool(0) = ", test >= test2)

print()
print("{0:=^50}".format("[CREATING DATATYPES FROM INHERITANCE]"))
# most of the times, the classes that we create are often mutable. But when when we inherit from an immutable class, we might need to overwrite the
# __new__ method because the object is baked into the object during creation and cannot be changed afterwards
# so in this case, we need to make sure our value is instantiated with the object alongside the creation time of the object
class FuzzyBoolean(float):
    def __new__(cls, x):
        return super().__new__(cls, x if 0.0 <= x <= 1.0 else 0.0)
    
    def __invert__(self):
        return FuzzyBoolean(1.0 - float(self))
    
    # we have reimplement the repr method else the float version will be used
    def __repr__(self) -> str:
        return "{0}({1})".format(self.__class__.__name__, super().__repr__())
    
    # in this class, we dont want all the arithmetic operations that is supported by floats to be present in our class
    # in this case, I will have to unimplement them 
    # since there are lots of them, I will have to make use of the exec method which takes a string and executes it in the current block context
    for name, operator in (("__add__", "+"), ("__sub__", "-"), ("__mul__", "*"),
                        ("__truediv__", "/"), ("__floordiv__", "//"), ("__mod__", "%"),
                        ("__imod__", "%="), ("__iadd__", "+="), ("__isub__", "-="),
                        ("__imul__", "*="), ("__itruediv__", "/="), ("__ifloordiv__", "//=")):
        message = "Unsupported operand types for {0}: '{{self}}' and '{{other}}'".format(operator)
        exec("def {0}(self, other):\n"
        "    raise TypeError(\"{message}\".format(self=self, other=other))".format(name, message=message)
        )

print("Creating object by inheriting from type float:") 
isTrained = FuzzyBoolean(3.0)
isTested = FuzzyBoolean(1.0)
try:
    print(isTested + isTrained)
except TypeError as e:
    print(f"'FuzzyBoolean(1.0)' + 'FuzzyBoolean(0.0) caused {e.__class__.__name__}")

print(f"the inverse of {isTrained!r} is", ~isTrained)

print()
print("Creating object by inheriting from type str:")

# here is a super string class that inherits from str class and adds some extra attributes to the object
# superstring allows for the creation of different type of strings that has default colors which cannot be changed, 
class SuperString(str):
    def __new__(cls, value, color:str = 'default', *args, **kwargs):
        color_codes = {
            'default': '\033[0m',
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m'
        }
        assert color.lower() in color_codes, "Invalid color specification"
        text_color = color_codes[color]
        value = text_color + value + ''
        return super().__new__(cls, value)

    def __init__(self, value, color :str='default') -> None:
        self.length = len(self)
        self.__text_color = color
    
    def __str__(self) -> str:
        return super().__str__() + '\033[0m'
    
    def __add__(self, other):  # implementing concatenation
        return SuperString(self.__str__() + SuperString(other.__str__(), self.__text_color))
    

    

print("Given the string:name = {}".format("'habib'"))
name = SuperString('habib', color="red")
print("calling name.length", name.length)

full_name = name + " Amoto"  
print(f"full_name = {name} + ' Amoto' ->" , full_name)

print()
print("{0:=^50}".format("[CREATING COLLECTION TYPES FROM SCRATCH]"))

# for the sake of this lesson, two error classes are created
class InvalidCoordinateError(Exception):pass


class NoFilenameError(Exception):pass


class SaveError(Exception):pass

class LoadError(Exception):pass


class Image:
    def __init__(self, width, height, filename='',  background="#ffffff") -> None:
        self.filename = filename
        self.__width = width
        self.__height = height
        self.__background = background
        self.__data = {}
        self.__colors = {self.__background}  # this is used to keep track of all the unique colors that is used in the Image

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def background(self):
        return self.__background
    
    @property
    def colors(self):
        return self.__colors
    
    def __getitem__(self, coordinate):
        assert len(coordinate) == 2, "Invalid Coordinate supplied, coordinate must be equal to 2"
        if (coordinate[0] < 0 or coordinate[0] > self.__width) or (coordinate[1] < 0 or coordinate[1] > self.__height):
            raise InvalidCoordinateError
        return self.__data.get((coordinate[0], coordinate[1]), self.__background)
    
    def __setitem__(self, coordinate, color):
        assert len(coordinate) == 2, "Invalid Coordinate supplied, coordinate must be equal to 2"
        if (coordinate[0] < 0 or coordinate[0] > self.__width) or (coordinate[1] < 0 or coordinate[1] > self.__height):
            raise InvalidCoordinateError
        self.__data[coordinate] = color
        self.__colors.add(color)

    def __delitem__(self, coordinate):
        assert len(coordinate) == 2, "Invalid Coordinate supplied, coordinate must be equal to 2"
        if (coordinate[0] < 0 or coordinate[0] > self.__width) or (coordinate[1] < 0 or coordinate[1] > self.__height):
            raise InvalidCoordinateError
        self.__data.pop(coordinate, None)
    
    def save(self, filename=None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError
        # opening the file to save the data that we have
        try:
            with open(self.filename, 'wb') as file:
                data = [ self.__width, self.__height, self.__background, self.__data ]
                pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)
        except (pickle.PickleError, EnvironmentError) as err:
            raise  SaveError(err)
        
    def load(self, filename=None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError
        
        # opening the given filename to load the data from it
        try:
            with open(self.filename, 'rb') as file:
                data = pickle.load(file)
                self.__width, self.__height, self.__background, self.__data = data
                self.__colors = set(self.__data.values()) | {self.__background}
        except (EnvironmentError, pickle.PickleError) as err:
            raise LoadError(str(err))
        

