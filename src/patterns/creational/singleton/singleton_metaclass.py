# SINGLETON METACLASS
# this allows to define a singleton similarly to the decorator but with a metaclass
import random


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print(f"Initializing database instance {random.randint(0, 100)}")


d1 = Database()
d2 = Database()
print(d1 == d2)
