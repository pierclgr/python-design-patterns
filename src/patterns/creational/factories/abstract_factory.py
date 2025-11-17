# Abstract factory: if you have a hierarchy of types, you can have a hierarchy of
# factories, and so you'll have an abstract factory at a certain point
from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink:
    @abstractmethod
    def consume(self):
        pass


class Coffee(HotDrink):
    def consume(self):
        print("Coffee consumed")


class Tea(HotDrink):
    def consume(self):
        print("Tea consumed")


# the following is the abstract factory class for the HOtDrink
class HotDrinkFactory(ABC):
    # factory method
    @abstractmethod
    def make(self, amount):
        raise NotImplementedError


class CoffeeFactory(HotDrinkFactory):
    def make(self, amount):
        print(f"Grind coffe, put filter, pour {amount}ml of hot water, filter "
              f"and serve!")
        return Coffee()


class TeaFactory(HotDrinkFactory):
    def make(self, amount):
        print(f"Pour {amount}ml of hot water, put tea bag, wait and serve!")
        return Tea()


def make_drink(drink):
    if drink == "tea":
        tf = TeaFactory()
        return tf.make("100")
    elif drink == "coffee":
        cf = CoffeeFactory()
        return cf.make("50")
    else:
        return None


# The make_drink method works but is not the best solution as:
# 1. breaks the open/closed principle
# 2. we need to instantiate a different factory for every drink
# 3. we're not using the abstract class but just using it as an interface

# we're going to create another class whose specific purpose is to instantiate the
# factories and objects
# class HotDrinkMachine:
#     # this still violates OCP as for every new drink it is needed to modify the
#     # following Enum class
#     class AvailableDrink(Enum):
#         COFFEE = auto()
#         TEA = auto()
#
#     factories = {}
#     initialized = False
#
#     def __init__(self):
#         if not self.initialized:
#             print("Initializing factories...")
#             for drink in self.AvailableDrink:
#                 capitalized_drink_name = drink.name.lower().capitalize()
#                 self.factories[capitalized_drink_name] = eval(
#                     capitalized_drink_name + "Factory")()
#
#     def make_drink(self):
#         print("Available drinks:")
#         i = 1
#         for drink in self.factories.keys():
#             print(f"{i}) {drink}")
#             i += 1
#
#         chosen_drink = int(input("Choose a drink number: "))
#         drink_factory = list(self.factories.values())[chosen_drink - 1]
#         amount = int(input("Specify the amount in ml: "))
#         return drink_factory.make(amount)

# As said, this still breaks the open-closed principle since we need to modify the enum
# to add another drink. To solve this problem, and be compliant with the open-closed
# principle, we can do the following
class HotDrinkMachine:
    # this still violates OCP as for every new drink it is needed to modify the
    # following Enum class
    factories = {}
    initialized = False

    @classmethod
    def register_factory(cls, name):
        drink = name.lower()
        factory = drink.capitalize() + "Factory"
        cls.factories[drink] = eval(factory)()
        return cls

    def make_drink(self):
        print("Available drinks:")
        i = 1
        for drink in self.factories.keys():
            print(f"{i}) {drink.capitalize()}")
            i += 1

        chosen_drink = int(input("Choose a drink number: "))
        drink_factory = list(self.factories.values())[chosen_drink - 1]
        amount = int(input("Specify the amount in ml: "))
        return drink_factory.make(amount)


machine = HotDrinkMachine()
machine.register_factory("coffee")
machine.register_factory("tea")


# this way, we simply need to extend the abstract classes HotDrink class and
# HotDrinkFactory to add a new drink and then add the drink to the machine
class Chocolate(HotDrink):
    def consume(self):
        print("Hot chocolate consumed")


class ChocolateFactory(HotDrinkFactory):
    def make(self, amount):
        print(f"Pour {amount}ml of hot milk, put hot chocolate, wait and serve!")
        return Chocolate()


machine.register_factory("chocolate")
machine.make_drink()
