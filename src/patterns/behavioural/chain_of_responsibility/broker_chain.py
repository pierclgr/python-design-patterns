# event broker (observer)
# command-query separation
from abc import ABC, abstractmethod
from enum import Enum
from unittest.case import DIFF_OMITTED


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.what_to_query = what_to_query
        self.value = default_value
        self.creature_name = creature_name


# this is the event broker, which takes care of the chain of responsibility
# this class will handle the queries by the user
class Game:
    def __init__(self):
        # this is the chain of responsibilities (it's a list with callable items)
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    @abstractmethod
    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1


class Creature:
    def __init__(self, game, name, attack, defense):
        self.initial_attack = attack
        self.initial_defense = defense
        self.game = game
        self.name = name

    # implement query to get attack value
    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name}: {self.attack}/{self.defense}"


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, "Strong Goblin", 2, 2)
    print(goblin)

    # this will add to the game's event the double attack modifier, so game.queries member which is of class Event
    # will have an item of DoubleAttackModifier (the object dam) in it
    dam = DoubleAttackModifier(game, goblin)

    # this means that when we call the method print, the __str__ method of the creature class will call the queries
    # to get the attack and defense values, which in turn will call the game.perform_query method which in turn will
    # call (by means of self.queries object, the DoubleAttackModifier.handle event, with the sender being the goblin
    # and the query having the creature initial_attack as value
    # the self.handle will then modify the query.value by doubling it and the property will finish the return
    print(goblin)

    dam2 = DoubleAttackModifier(game, goblin)
    print(goblin)

    with IncreaseDefenseModifier(game, goblin):
        # this modifier will work only inside this scope
        print(goblin)
    print(goblin)
