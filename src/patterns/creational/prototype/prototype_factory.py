# Prototype Factory
# The prototype factory is a pattern that uses factories alongside prototypes to create
# objects by cloning and then modifying prototypes
from copy import deepcopy

class Address:
    def __init__(self, street, suite, country):
        self.street = street
        self.suite = suite
        self.country = country

    def __str__(self):
        return f"Address(street={self.street}, suite={self.suite}, country={self.country})"

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Employee(name={self.name}, address={self.address})"

class EmployeeFactory:
    # these are the prototypes to use for the employees
    main_office_employee = Employee("", Address("123 London Road", 0, "UK"))
    aux_office_employee = Employee("", Address("123 Another Road", 0, "USA"))

    # private factory method for employees, copying a given prototype
    @staticmethod
    def __new_employee(prototype, name, suite):
        employee_clone = deepcopy(prototype)
        employee_clone.name = name
        employee_clone.address.suite = suite
        return employee_clone

    # factory methods for the two offices
    @classmethod
    def new_main_office_employee(cls, name, suite):
        return cls.__new_employee(cls.main_office_employee, name, suite)

    @classmethod
    def new_aux_office_employee(cls, name, suite):
        return cls.__new_employee(cls.aux_office_employee, name, suite)

jane = EmployeeFactory.new_main_office_employee("Jane", 121)
mark = EmployeeFactory.new_main_office_employee("Mark", 553)
john = EmployeeFactory.new_aux_office_employee("John", 223)
print(jane)
print(mark)
print(john)