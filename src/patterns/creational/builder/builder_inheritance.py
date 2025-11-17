# This solves the Builder Facet pattern's violation of the open-closed principle
class Person:
    def __init__(self):
        self.__name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return (f"Person(name={self.name}, position={self.position}, "
                f"date_of_birth={self.date_of_birth})")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @staticmethod
    def create() -> "PersonBuilder":
        return PersonBuilder()


# default PersonBuilder simply initializing the person
class PersonBuilder:
    def __init__(self, person: Person = None):
        if not person:
            person = Person()
        self.person = person

    def build(self) -> Person:
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def name(self, name: str):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def job(self, job):
        self.person.position = job
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    def birth_date(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


me = PersonBirthDateBuilder()\
    .name("John")\
    .job("Software Engineer")\
    .birth_date("1990-01-01")\
    .build()
print(me)