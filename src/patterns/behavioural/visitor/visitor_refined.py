# The accept method is not needed now
from abc import ABC


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class SubtractionExpression(AdditionExpression):
    pass


# Visitor object
class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    # method overloading with parameters definition
    @visitor(DoubleExpression)
    def visit(self, de):
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.buffer.append('(')
        self.visit(ae.left)
        self.buffer.append("+")
        self.visit(ae.right)
        self.buffer.append(")")

    @visitor(SubtractionExpression)
    def visit(self, se):
        self.buffer.append('(')
        self.visit(se.left)
        self.buffer.append("-")
        self.visit(se.right)
        self.buffer.append(")")

    def __str__(self):
        return "".join(self.buffer)


class ExpressionEvaluator:
    def __init__(self):
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, de):
        self.value = de.value
        return self.value

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.value = self.visit(ae.left) + self.visit(ae.right)
        return self.value

    @visitor(SubtractionExpression)
    def visit(self, se):
        self.value = self.visit(se.left) - self.visit(se.right)
        return self.value

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    e = AdditionExpression(
        DoubleExpression(1),
        SubtractionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    printer = ExpressionPrinter()
    printer.visit(e)

    evaluator = ExpressionEvaluator()
    evaluator.visit(e)

    print(f"{printer} = {evaluator}")
