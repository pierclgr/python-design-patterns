class Event(list):  # class Observer
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()

class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        # this notifies the changing of a property
        self.property_changed('age', value)

class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        self.person.property_changed.append(
            self.person_changed
        )

    def person_changed(self, name, value):
        if name == "age":
            if value >= 16:
                self.person.property_changed.remove(self.person_changed)
                print("You can now drive")
            else:
                print("You are too young to drive")

if __name__ == "__main__":
    p = Person(13)
    tra = TrafficAuthority(p)

    # the changing of the age triggers the person_changed method, which was added to the list of events in the person
    # class (through PropertyObservable)
    p.age = 14
    p.age = 15

    # from here on, we should only be notified once
    p.age = 16
    p.age = 17
    p.age = 18