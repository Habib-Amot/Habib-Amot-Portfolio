# say we want to create a Point object in python. This object holds the value of x and y
import math 

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def distance_from_origin(self) -> float:
        return math.hypot(self.x, self.y)
    
    def __eq__(self, other) -> bool:
        try:
            return self.x == other.x and self.y == other.y
        except AttributeError:
            return NotImplemented
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    
    def __str__(self) -> str:
        return "({0.x}, {0.y})".format(self)

p = Point(34, 29)
b = Point(23, 45)

if __name__ == "__main__":
    print("the representational form of point p is:", repr(p))
    print("the string form of point p is:", str(p))
    print("the hypothenus of p is ", p.distance_from_origin())

    # now we can make comparisons between the two objects
    print('p = b is ', b == p)
