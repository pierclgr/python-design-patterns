# Interface Segregation Principle (IPS)
# An interface should NOT contain too many methods and elements
from abc import abstractmethod, ABC

# making interface with too many elements is not a good idea since you're forcing
# the client to define methods that it doesn't even need
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionPrinter(Machine):
    # this is ok
    def print(self, document):
        pass

    # this is not ok as it is old-fashioned
    def fax(self, document):
        pass  # NOOP

    # this is not ok as it is old-fashioned
    def scan(self, document):
        raise NotImplementedError('Printer cannot scan!')

# this solves the problem above
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        pass

class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass

# interface
class MultiFunctionDevice(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

# interface implementation
class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
