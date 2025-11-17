# Open/Closed Principle (OCP)
# Open for extension, closed for modification
from enum import Enum
from abc import abstractmethod
from typing import Collection, Any, Generator


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    # This violates Open/Closed Principle
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p


# Specification pattern
# specification is a class that defines whether an object satisfies a condition or not
class Specification:
    @abstractmethod
    def is_satisfied(self, item: Product):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    @abstractmethod
    def filter(self, items: Collection[Product], spec: Specification):
        pass


class ColorSpecification(Specification):
    def __init__(self, color: Color) -> None:
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size) -> None:
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        return item.size == self.size


# Combinator
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item: Product):
        # "all" ANDs all conditions in the parenthesis
        # "map" maps all the specifications to the item, such specifications are in the
        # args
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items: Collection[Product], spec: Specification) -> Generator:
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product(name="Apple", color=Color.GREEN, size=Size.SMALL)
    tree = Product(name="Tree", color=Color.GREEN, size=Size.LARGE)
    house = Product(name="House", color=Color.BLUE, size=Size.LARGE)

    products = [apple, tree, house]

    # THIS BREAKS OCP
    print("This breaks OCP")
    print("Green products (old):")
    pf = ProductFilter()
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f"- {p.name} is green")

    print("Large products (old)")
    for p in pf.filter_by_size(products, Size.LARGE):
        print(f"- {p.name} is large")

    print("Large blue products (old)")
    for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.BLUE):
        print(f"- {p.name} is large and blue")

    # This doesn't break OCP
    print("This doesn't break OCP")
    print("Green products (new):")
    bf = BetterFilter()
    is_green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, is_green):
        print(f"- {p.name} is green")

    print("Large products (new)")
    is_large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, is_large):
        print(f"- {p.name} is large")

    print("Large blue products (new)")
    # is_large_and_blue = AndSpecification(
    #     is_large,
    #     ColorSpecification(Color.BLUE)
    # )
    is_large_and_blue = is_large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, is_large_and_blue):
        print(f"- {p.name} is large and blue")
