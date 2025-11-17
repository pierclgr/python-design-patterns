# Flyweight pattern
# The flyweight pattern is used to reduce the memory usage by reducing redundancies and saved objects. The data is
# stored externally and referred to from attributes/variables.
import string, random


# this is to simulate names
def random_string():
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for _ in range(8)])


# class User:
#     def __init__(self, name):
#         self.name = name
# here, a lot of names generated randomly will be the same, so over large number of users we're going to waste a lot
# of memory
# we can use flyweight pattern to reduce the memory usage
class User:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(" ")]

    def __str__(self):
        return " ".join([self.strings[x] for x in self.names])


if __name__ == "__main__":
    user = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first in first_names:
        for last in last_names:
            user = User(f"{first} {last}")
            print(user)

# this way, we're memorizing only ONCE each unique random string, saving memory, and when we need it we simply use the
# variable or attribute to refer to it; hence, we're not instantiating multiple copies of the same unique string
