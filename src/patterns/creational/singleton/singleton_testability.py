import unittest

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.populations = {
            "New York": 8_419_000,
            "Los Angeles": 3_971_000,
            "Chicago": 2_716_000,
            "Houston": 2_326_000,
            "Phoenix": 1_680_000,
        }

class DummyDatabase:
    def __init__(self):
        self.populations = {
            "New York": 8_419_000,
            "Los Angeles": 3_971_000
        }

class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            # following line will access always the same object due to the singleton
            # capabilities provided through the metaclass

            # setting it by this will however FORCE us to use that and only that
            # instance of the DB
            result += Database().populations[c]

        return result

# instead, we'll define a better record finder whose initialized receives a database
# that we can specify
class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            # following line will access always the same object due to the singleton
            # capabilities provided through the metaclass
            result += self.db.populations[c]

        return result

class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ["New York", "Los Angeles"]
        result = rf.total_population(names)
        self.assertEqual(result, 12_390_000)

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(12_390_000, crf.total_population(["New York", "Los Angeles"]))

if __name__ == "__main__":
    unittest.main()