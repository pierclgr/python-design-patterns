# Proxy Pattern
# The proxy pattern provides a substitute object for another object that has the same interface but different behaviour
# underneath it. This way, the proxy adds functionality without changing the interface.

# The most common proxy is the protection proxy, which is used to control the access to an object.

class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")

class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# let's say that we want now to add a control over the age of the driver, to block the car being driven by underaged
# if we modify the car class, we break the OCP, so instead we use the proxy pattern, with interface matching the Car
# class

class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.__car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.__car.drive()
        else:
            print("Driver too young")

if __name__ == "__main__":
    john = Driver("john", 45)
    car = Car(john)
    car.drive()

    car = CarProxy(john)
    car.drive()

    jane = Driver("jane", 15)
    car = CarProxy(jane)
    car.drive()