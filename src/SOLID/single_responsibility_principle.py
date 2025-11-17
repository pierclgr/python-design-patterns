# SRP: Single Responsibility Principle
# SOC: Separation of Concerns
# Each class will take a PRIMARY RESPONSIBILITY and should not take on any other
# responsibility
# SRP breaks the GOD object problem

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # These methods break SRP/SOC: Journal should not be responsible for persistence
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today")
j.add_entry("I ate a bug.")
print(j)

file = "test.txt"
PersistenceManager.save_to_file(j, file)
with open(file) as f:
    print(f.read())
