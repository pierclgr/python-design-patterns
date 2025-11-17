# State Pattern
# The state pattern is used to represent the state of something; this state could change and evolve depending on events
# and things happening, and an object often transitions from one state to another when triggered.
from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def on(self, switch):
        pass

    @abstractmethod
    def off(self, switch):
        pass


class OnState(State):
    def __init__(self):
        print("Light turned on")

    def off(self, switch):
        switch.state = OffState()

    def on(self, switch):
        print("Light is already on")


class OffState(State):
    def __init__(self):
        print("Light turned off")

    def off(self, switch):
        print("Light is already off")

    def on(self, switch):
        switch.state = OnState()


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


if __name__ == "__main__":
    sw = Switch()
    sw.on()
    sw.on()
    sw.off()
    sw.off()
