# Decorator Pattern
# The decorator pattern exists to add functionalities to a class without inheriting
# from another one providing the functionality; this is done to keep the functionalities
# separated, accordingly to the OCP
import time

# decorator with parameters
def time_it(time_unit="ms"):
    # this is the internal decorato, which actually defines a "classic" decorator
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time() - start
            if time_unit == "ms":
                mult = 1000
            else:
                mult = 1
            print(f"{func.__name__} took {int(end * mult)}{time_unit}")

            return result
        return wrapper
    return decorator

# we can define time_it through python's decorator special syntax, to apply the wrapper
# to the function anytime you call it
# multiple decorators can be chained as
# @decorator2
# @decorator1
# def func():
#     pass

@time_it("s")
def some_op():
    print("Starting operation")
    time.sleep(1)
    print("Operation terminated")
    return 123

if __name__ == "__main__":
    # without python decorator
    # some_op = time_it("ms")(some_op)()

    # with python decorator
    some_op()