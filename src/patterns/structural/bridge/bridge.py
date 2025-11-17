# Bridge Pattern
# The bridge pattern avoids the problem of exploding complexity when implementing
# subclasses for different scenarios: it separates the interfaces from the
# implementation, allowing to change then independently

# let's say that we have a circle and square which can be both raster or vector
# this will lead us to 4 classes
# VectorSquare, RasterSquare, VectorCircle, RasterCircle
# bridge pattern solves this problem by splitting the concepts in shapes (Circle Square)
# and renderers (Vector Raster), while bridge pattern connects these two concepts
from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Rendering a circle with radius {radius}")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Rendering pixels for a circle with radius {radius}")

class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def resize(self, factor): pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        # this is where we're going to use the Bridge
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

# a bridge connects two different hierarchies by using a parameter of one of the two
# hierarchies as an object of the other hierarchy in the constructor (in this example,
# the renderer is an object of the renderer hierarchy in the constructor of the shape)

# the bridge pattern violates the OCP because, for example, if we want to add a shape
# we need to implement a render method for that particular shape in all of the
# renderer hierarchies; also, if we add another renderer, we also need to implement all
# the render methods for that new class

if __name__ == "__main__":
    vr = VectorRenderer()
    rr = RasterRenderer()
    circle = Circle(vr, 100)
    circle.draw()
    circle = Circle(rr, 5)
    circle.draw()