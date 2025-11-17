# the most classic use of decorators is a class that can be used to decorate with
# additional functionalities another class
from abc import ABC

class Shape(ABC):
    def __str__(self):
        return ""

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"A circle of radius {self.radius}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A square with side {self.side}"

# we can add functionalities to the shapes by defining other classes
class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"

class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has {int(self.transparency*100)}% transparency"

if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    # this decoratest the class circle with additional functionalities
    red_circle = ColoredShape(circle, "red")
    print(red_circle)

    red_half_transparent_circle = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_circle)

    # the problem is that we can add the same decorator twice
    # (e.g. ColorShape(ColorShape(circle, "red"), "blue"))
    # this can be treated through exceptions in ColorShape constructor, but it is
    # difficult to catch all the cases

    # also, it is impossible to access base class methods (e.g. circle's resize) when
    # these objects are decorated

    # however, in OOP, a decorator is simply a class wrapping another class