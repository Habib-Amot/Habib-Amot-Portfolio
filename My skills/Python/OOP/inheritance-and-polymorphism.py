# in this lesson I am going to learn and understand Inheritance and Polymorphism in python
# Inheritance is the process in which a child class (subclass) inherit from a parent class (base class, superclass)
# when we do this, all the properties of the parent class becomes available in the child class when not overwritten
# I will be using the Point class in this lesson

import math
from attribute_and_methods import Point

# creating a cirlce class that inherits from the Point class
class Circle(Point):
    def __init__(self, radius, x, y) -> None:
        super().__init__(x, y)
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * math.pow(self.radius, 2)
    
    def circumferece(self) -> float:
        return 2 * math.pi * self.radius
    
    def edge_distance_from_origin(self) -> float:
        return abs(self.distance_from_origin() - self.radius)
    
    def __repr__(self) -> str:
        return "Circle({0.radius}, {0.x}, {0.y})".format(self)
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, other) -> bool:
        return super().__eq__(other) and self.radius == other.radius



# now we can make use of this class by instantiating and object of it
circle1 = Circle(12, 40, 30)
circle2 = Circle(12, 40, 30)
circle3 = Circle(12, 40, 35)
point1 = Point(40, 30)
print("calling distance_from_origin from Circle1 ",circle1.distance_from_origin())
print("calling distance_from_origin from Point1 ", point1.distance_from_origin())

print("comparing objects:")
print(f"comparing {repr(circle1)} = {repr(circle2)}", circle1 == circle2)
print(f"comparing {repr(circle2)}) = {repr(circle3)}", circle2 == circle3)

# inheritance is the feature that makes an object behave as though it belongs to another class that is different from it base class
# this allow us to create objects that behave like another object of another class. And also provides an interface that any function or methods can plug into
# from our example above, the Cicle class behaves similary to the Point class in terms of certain operation

print()
print("{0:=^40}".format("[POLYMORPHISM]"))
# Polymorphism is a feature in OOP that allows different object to behave in the same way even though they are not internally. They provide
# interface(s) that make any object to work with them as if they are familiar with the polymorphic object. 

# below is an example of a mini payment system
class PaymentMethod:
    def __init__(self):
        self.card_name = self.__class__.__name__
    
    def process_payment(self, **details):
        # the base class cannot process payment it has to be overidden by child classes
        raise NotImplementedError
    

class PaypalCard(PaymentMethod):
    def __init__(self):
        super().__init__()
        
    def process_payment(self, **details):
        print("processing payment using details: {details}".format(details=details))


class CreditCard(PaymentMethod):
    def __init__(self):
        super().__init__()

    def process_payment(self, **details):
        print("processing payment using details {0}".format(details))


# now can can have a function that takes any object and calls the process payment method
def process_card(obj: PaymentMethod, **details):
    # initiating the transaction using the obj
    print("Starting transaction using {0.card_name}".format(obj))
    obj.process_payment(**details)

card1 = CreditCard()
card2 = PaypalCard()

print("processing the first card by calling the process payment method:")
process_card(card1, name="Amot The Dev", amount=500, from_acc="12378", to_acc="12345", bank_name="Afri Bank")
print()
print("processing the second card by calling the process payment method:")
process_card(card2, name="Amot The Dev", amount=1000, from_acc="120078", to_acc="12000", bank_name="Afri Bank")



print()
print("{0:=^90}".format("[USING PROPERTIES(getters, setters and deleters) FOR ATTRIBUTES ACCESS]"))
# lets create another version of the Cicle class but this time, the properties will be accessed just like an attribute. This can be achieved using 
# getter which is gotten by making use of @property decorator

class Circle2(Point):
    def __init__(self, radius: float, x: float, y: float) -> None:
        super().__init__(x, y)
        self.__radius = radius  # this attribute is still accessbile by calling .radius. to make it inaccessible, we use setters

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        # creating an assertion to make sure that the radius that is being passed is a valid one and not a non-zero value
        assert radius > 0, "radius must be greater than 0"
        self.__radius = radius


test = Circle2(23, 45, 21)
print("accessing attribute radius from Circle2", test.radius)
# now the radius attribute can also be set
try:
    test.radius = 0  # this will cause an assertion error
except AssertionError:
    print("pass a valid value as radius")

# this time a valid radius
test.radius = 30
print(test.radius, "is the new value of radius after changing")
    
