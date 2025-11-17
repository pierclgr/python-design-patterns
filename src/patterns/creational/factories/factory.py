# Factory pattern
# Once you get too many factor methods inside a class, it makes sense to apply the
# single responsibility principle and add move these factory methods under a grouping
# singular entity, which is in fact the Factory class.
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # inner factory class
    class PointFactory:
        # factory methods - can be non-static if the factory class holds some kind of
        # state too
        def create_cartesian_point(self, x, y):
            return Point(x, y)

        def create_polar_point(self, rho, theta):
            # here, a conversion from polar to cartesian coordinates happen
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    # this is now a CLASS attribute which is available for all the Point objects
    factory = PointFactory()

# it can be made also an outer class
# class PointFactory:
#     # factory methods
#     @staticmethod
#     def create_cartesian_point(x, y):
#         return Point(x, y)
#
#     @staticmethod
#     def create_polar_point(rho, theta):
#         # here, a conversion from polar to cartesian coordinates happen
#         return Point(rho * math.cos(theta), rho * math.sin(theta))

p1 = Point.factory.create_cartesian_point(2, 3)
p2 = Point.factory.create_polar_point(1, 2)
print(p1)
print(p2)


# now you have a dedicated entity whose responsibility is to build the points, while
# an entity whose only responsibility is to represent the point, so similarly to
# the Builder but here the "building" simply means initializing. It can be mo