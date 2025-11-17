# SINGLETON DECORATOR
# this is used to solve the problem with singleton allocator of __init__ method being
# called twice

# define a singleton decorator as a function that keeps an history of instances of objects
# that want to still be singleton
import random


def singleton(class_):
    print(class_)
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            print(f"Initializing {class_}")
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print(f"Initializing database instance {random.randint(0, 100)}")


d1 = Database()
d2 = Database()
print(d1 == d2)
