# python decorators can also be applied to class methods and classes itself, to enhance the capabilities of classes
# without touching the internal code
def add_repr(cls):
    def __repr__(self):
        return f"{cls.__name__}({self.__dict__})"

    cls.__repr__ = __repr__
    return cls


# now, I can use add_repr to add a representation to any class
@add_repr
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


# this equals to redefining the class Person as
# Person = add_repr(Person)

if __name__ == "__main__":
    p = Person("Alice", "Rossi")
    print(p)
