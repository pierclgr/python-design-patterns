# MONOSTATE
# A variation of the singleton pattern in which all the state of an object is put into
# a static variable.

class CEO:
    __shared_state = {
        "name": "Steve",
        "age": 55
    }

    def __init__(self):
        # the init method will assign to the object's set of attributes the shared state
        # by coping the reference of the shared state
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"CEO: {self.name}, {self.age}"

# ceo1 = CEO()
# print(ceo1)
#
# ceo2 = CEO()
# ceo2.age = "77"  # this will change the state of both the CEOs objects
# print(ceo1)
# print(ceo2)


# we can also define the monostate as a class
class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

# to implement monostate functionalities, then, we can simply inherit from this class
class CFO(Monostate):
    def __init__(self):
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return f"CFO: {self.name}, {self.money_managed}"

cfo1 = CFO()
cfo1.name = "Sheryl"
cfo1.money_managed = 1
print(cfo1)

cfo2 = CFO()
# again this modifies both cfo1 and cfo2 as they share the same state
cfo2.name = "John"
cfo2.money_managed = 10
print(cfo2)
print(cfo1)
