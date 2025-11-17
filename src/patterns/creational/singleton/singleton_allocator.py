# Singleton
# The singleton is a pattern made for such objects that only need to be instanced once
# through the whole program flow (e.g. factories, database instances, resources
# representation etc.). Singleton allows to have only one instance for an object,
# avoiding re-instantiation and copies.

# SINGLETON ALLOCATOR
# The first way to implement the singleton is by re-writing the allocator
import random


class Database:
    _instance = None

    def __init__(self):
        print(f"Initializing database instance {random.randint(0, 100)}")

    # this method allows for instantiation of objects of this class only once
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


d1 = Database()
d2 = Database()
print(d1 == d2)

# this class however still calls the init method twice, even though the object is just
# once in the end
