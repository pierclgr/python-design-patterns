# Factory pattern delegates the whole creation of an object to another entity, like a
# method, a class or an object.
# Differently from the Builder, it doesn't take responsibility for the piece by piece
# initialization of the object, but rather it takes responsibility for the creation of
# the wholesale object.
# I.E.:
# - Builder handles INTERNAL initialization of the object (within __init__)
# - Factory handles EXTERNAL initialization of the object (handles __init__ calling)

# FACTORY METHOD
# factory methods are alternatives to initializers that allow for different
# initializations of objects of the same class;
# since you can't define different __init__ constructors with different parameters and
# meanings, factory methods help you in doing so
import math

# class Point:
#     def __init__(self, x, y, point_type):
#         if point_type == "cartesian":
#             self.x = x
#             self.y = y
#         elif point_type == "polar":
#             self.x = x * math.cos(y)
#             self.y = x * math.sin(y)
# this class is too complicated because the more alternatives we have, the more
# additional parameters we need to pass to the constructor, making it less and less
# maintainable, clear and simple
# we can use factory methods to solve this issue, by writing different "init"
# substitutors with different names and parameters

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # factory methods
    @staticmethod
    def create_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def create_polar_point(rho, theta):
        # here, a conversion from polar to cartesian coordinates happen
        return Point(rho * math.cos(theta), rho * math.sin(theta))

p1 = Point.create_cartesian_point(2, 3)
p2 = Point.create_polar_point(1, 2)

print(p1)
print(p2)
