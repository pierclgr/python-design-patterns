# Dependency Inversion Principle (DIP)
# High-level modules in the code should not depend on low-level modules but on higher
# level abstractions (interfaces)
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


# class Relationships:
#     def __init__(self):
#         self.relations = []
#
#     def add_parent_and_child(self, parent, child):
#         self.relations.append(
#             (parent, Relationship.PARENT, child)
#         )
#         self.relations.append(
#             (child, Relationship.CHILD, child)
#         )
#
#
# class Research:
#     def __init__(self, relationships):
#         relations = relationships.relations
#         for r in relations:
#             if r[0].name == 'John' and r[1] == Relationship.PARENT:
#                 print(f'John has a child called {r[2].name}')

# in this case, the high level module Research DEPENDS on the implementation of
# Relationships' relations, being it a list. This is a problem because if you change
# Relationships' relations implementation, the code will not work anymore
# Research depends on the concrete implementation (low-level module) Relationships while
# it should depend on an Abstraction

# parent = Person('John')
# child = Person('Chris')
# child2 = Person('Matt')
#
# relationships = Relationships()
# relationships.add_parent_and_child(parent, child)
# relationships.add_parent_and_child(parent, child2)
#
# r = Research(relationships)

# interface abstraction
class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # low-level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, child)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

# in this case, you simply need to re-write the concrete implementation of
# find_all_children_of, while the client which uses the Abstraction will not depend
# on it

class Research:  # high-level module
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')

parent = Person('John')
child = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child)
relationships.add_parent_and_child(parent, child2)

r = Research(relationships)
