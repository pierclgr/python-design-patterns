# LSP (Liskov Substitution Principle)
# If S is a subclass of T, then objects of type T may be replaced with objects of type S

class Rectangle:
    def __init__(self, width, height):
        # protected attributes (only accessible by class and subclasses
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"


# this class breaks LSP
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


# according to LSP, you should be able to use a Square as a Rectangle
def use_it(rc):
    w = rc.width
    rc.height = 10
    expected_area = w * 10
    print(f"Expected area: {expected_area}, actual area: {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

# Square class breaks LSP
sq = Square(5)
use_it(sq)
