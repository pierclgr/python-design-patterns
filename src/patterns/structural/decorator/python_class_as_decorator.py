# In python, classes can also be used as decorators themselves; it is used when you want to add a stateful and
# configurable behavior to your decorator
class Repeat:
    def __init__(self, n):
        self.n = n

    # this is the decorator method
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.n):
                print(f"Call {i + 1} of {self.n}")
                func(*args, **kwargs)
        return wrapper

# now, we can define a function using a class decorator
@Repeat(3)
def say_hello(name):
    print(f"Hello {name}")

# this is equal to writing
# Repeat(3)(say_hello)("Luigi")
# or to replacing the method say_hello as
# say_hello = Repeat(3)(say_hello)

# it is also possible to use class decorators to other classes
@Repeat(2)
class Wave:
    def __init__(self):
        print("Waving")

# which is equal to writing
# Wave = Repeat(2)(Wave)
# or to calling directly
# Repeat(2)(Wave)()

if __name__ == "__main__":
    say_hello("Pier")