# Now we have a visitor element (ExpressionPrinter print's method) that works separately from the Objects it visits,
# so DoubleExpression and AdditionExpression. Now, the printing logic is all handed separated from the objects. This
# matches the separation of concerns principle. This still violates OCP because if we want to add other expressions,
# we still need to modify ExpressionPrinter print's method
from abc import ABC, abstractmethod


class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')


class Expression(ABC):
    @abstractmethod
    def eval(self): pass

    def print(self, buffer):
        ExpressionPrinter.print(self, buffer)


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == "__main__":
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []
    e.print(buffer)
    print("".join(buffer), '=', e.eval())
