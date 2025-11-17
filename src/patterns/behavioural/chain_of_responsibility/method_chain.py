# Chain of responsibility
# This behavioural pattern is used to pass a request along a chain of potential handlers until one of them handles it

class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name}: {self.attack}/{self.defense}"


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    # this method chains methods call for the modifiers through next_modifier; if the latter is initialized, it calls
    # the method on it and "cascades" the following within next_modifier's add_modifier method
    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    # this methods chains methods call for the modifiers through next_modifier: if the latter is initialized, it calls
    # the method on it and "cascades" the following within next_modifier's handle method
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2

        # call the superclass method to continue the chain of modifiers, if any
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name} defense")
            self.creature.defense += 1

        # call the superclass method to continue the chain of modifiers, if any
        super().handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you")

        # by skipping the super().handle() call, the chain of responsibility is not applied and thus the applying of
        # following modifiers, if any, is skipped


if __name__ == "__main__":
    goblin = Creature("Goblin", 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)
    root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.handle()
    print(goblin)
