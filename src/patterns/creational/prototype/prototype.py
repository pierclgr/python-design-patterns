# Prototype patter
# The prototype pattern serves as a "prototype", so like a blueprint for objects that
# can be cloned to create new objects by customizing them. They're partially or fully
# initialized objects that can be copied (or cloned) and made use of.

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Person(name={self.name}, address={self.address})"

class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"Address(street={self.street}, city={self.city}, country={self.country})"

address = Address("123 London Road", "London", "UK")
john = Person("John", address)
jane = Person("Jane", address)
jane.address.street = "123 another road"

# this will modify bot addresses as "address" is a reference to the same object
from copy import deepcopy, copy
jane = deepcopy(john)  # deepcopy recursively copy the object and all the attributes
# josh = copy(john)  # copy will perform a shallow copy, so the object itself will be a
# clone but all the references (including "address") will not be copied
jane.name = "Jane"
jane.address.street = "123 London road"

print(jane)
print(john)

# this allows to use prototypes to create another object and then modifying it, by
# reusing existing objects