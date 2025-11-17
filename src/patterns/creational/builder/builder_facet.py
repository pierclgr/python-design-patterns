# The builder facet pattern allows to define different sub-builders to build different
# components of the same object when the initialization of this object is too
# complicated to the point where using only one builder would create a builder
# with too many parameters. This is done by creating a builder interface that handles
# the different sub builders.

class Person:
    def __init__(self):
        # address
        self.address = None
        self.postcode = None
        self.city = None

        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return (f"Person lives at {self.address}, {self.postcode} {self.city}.\nWorks "
                f"at {self.company_name} as a {self.position} earning "
                f"{self.annual_income}.")

    @staticmethod
    def create() -> "PersonBuilder":
        return PersonBuilder()


class PersonBuilder:
    def __init__(self, person: Person = None) -> None:
        if not person:
            person = Person()
        self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person = None):
        super(PersonJobBuilder, self).__init__(person)

    def at(self, company_name: str):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earns(self, annual_income: str):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person = None):
        super(PersonAddressBuilder, self).__init__(person)

    def at(self, address: str):
        self.person.address = address
        return self

    def in_city(self, city: str):
        self.person.city = city
        return self

    def with_postcode(self, postcode: str):
        self.person.postcode = postcode
        return self

# WARNING: the builder facet pattern violates the open-closed principle. This happens
# because whenever you need a new sub-builder, you need to modify the builder interface
# and add the property handling the new sub-builder
person = Person.create() \
    .lives \
    .at("123, London Road") \
    .in_city("London") \
    .with_postcode("12345") \
    .works \
    .at("OpenAI") \
    .as_a("Software Engineer") \
    .earns("100000") \
    .build()

print(person)
