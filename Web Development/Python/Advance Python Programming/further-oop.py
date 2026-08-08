# first in this lesson, I am going to be using the slot attribute of a class to control the property that an object has
# the __slot__attribute is what is checked first by python before the __dict__ attribute which contains each of the attribute that an object has
# below is an example

from typing import Any


print("{0:=^50}".format("[CONTROLLING OBJECT ATTRIBUTE WITH __SLOTS__]"))
class FixedData:
    __slots__ = ('name', 'age')  # object of this class only has name and age property

    def __init__(self: FixedData, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def full_data(self):
        return "Name: {}, Age: {}".format(self.name, self.age)
    


dev_amot = FixedData("Habib Amot", 25)
print(dev_amot.full_data())
# and now, any attempt to set a new property to the object, will be blocked
try:
    dev_amot.alias = "Amot The Dev"    # this will cause an attribute error
except AttributeError as e:
    print(e)

print()

print("{0:=^50}".format("[CONTROLLING OBJECT ATTRIBUTE ACCESS]"))
# anytime an attribute is accessed or set in python, the __getattr__ and __setattr__ are called respectively
# and also when an attribute is deleted, the __delattr__ is called as well

# this allows me to compute some values on the fly e.g
class PromiscousObj:
    # this class has no init method at first, but computes them during access
    def __setattr__(self, attr: str, value):
        if attr.isidentifier():
            self.__dict__[attr] = value

    def __delattr__(self, name: str) -> None:
        assert name in self.__dict__, "Object has no attribute {}".format(name)
        del self.__dict__[name]
    

prom1 = PromiscousObj()
print("this object does not have the last_name attribute before but was created on the fly")
prom1.last_name = 'agent smith'
print("prom1.last_name", prom1.last_name)

# this behavior can also be leveraged to create Constants


class Const:
    __slots__ = ('value')

    def __init__(self, value):
        self.value = value
    
    def __repr__(self) -> str:
        return "Const({self.value})".format(self=self)
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name not in self.__slots__:
            raise AttributeError("unable to set new value for Const object")
        elif hasattr(self, name):
            raise AttributeError('Const value can only be set once')
        super().__setattr__(name, value)
    
    def __delattr__(self, name: str) -> None:
        if name not in self.__slots__:
            raise AttributeError(f'object has not property {name}')   
        raise AttributeError("cannot delete object of type Const")

print()
age = Const(23)
name = Const("Habib Amot")
print('attempting to set and delete attribute from Const object name and age')
try:
    age.value = 10
    del name.value
except AttributeError as err:
    print("attempt was made to either delete Const attributes or set it", err)


print()
print("{0:=^50}".format("[FUNCTORS]"))
print("Functor is way of making an object callable by implementing the __call__ method of the object which makes the object to be called just like a function")
# one of the things that makes Functors useful is their ability to capture state data although this can still be achieved with closures
# e.g

class HeadingWriter:
    def __init__(self, format) -> None:
        self.__heading_format: str = format
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for arg in args:
            print(self.__heading_format.format(arg))

heading = HeadingWriter("{0:=^50}")
heading('[Functor]')
