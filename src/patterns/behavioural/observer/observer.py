# Observer Pattern
# The observer is used to notify other objects when something happens. It is then used to track changes in certain
# components of the system and notify other components accordingly.

# Observer relies on the concept of Events, which are specific objects recording something that happened or happens.
class Event(list):  # class Observer
    # it is a list of callable functions that are called when the event is triggered
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        # send the event
        self.falls_ill(self.name, self.address)


# now we build something that "subscribes" to the notifications of the event
def call_doctor(name, address):
    print(f"Call doctor for {name} at {address}")


if __name__ == "__main__":
    p = Person("John", "123 Baker street")

    # to the fall hill event of the person, we add the call doctor function so that when a person falls ill, a doctor
    # is automatically called; the event is fired by the catch_a_cold method
    p.falls_ill.append(lambda name, address: print(f"{name} at {address} got ill"))
    p.falls_ill.append(call_doctor)
    p.catch_a_cold()
    p.falls_ill.remove(call_doctor)
    p.catch_a_cold()
