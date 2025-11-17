# Visitor Pattern
# The visitor pattern is a pattern that defines a component (the visitor) that knows how to traverse a data structure
# composed of different types of objects. The target is to separate the algorithms from the objects over which they
# operate.

# The intrusive visitor violates the OCP because requires to modify classes to add new operations. In this case,
# we don't implement a visitor pattern, because we have a visitor method "print" that depends on the object type,
# whether it's a DoubleExpression or an AdditionExpression. This also violates the separation of concern principle
# due to the fact that printing and evaluation are mixed and handled by the same class.

class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self):
        return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append("+")
        self.right.print(buffer)
        buffer.append(')')

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
