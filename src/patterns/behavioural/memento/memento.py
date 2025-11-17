# Memento Pattern
# The memento pattern is used to memorize the changes of a certain object over time, by saving a "snapshot" of the
# system state at every time. Memento then provides a way to roll back to a certain state in time.

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         return Memento(self.balance)
#
#
#     def restore(self, memento):
#         self.balance = memento.balance
#
#     def __str__(self):
#         return f"Balance = {self.balance}"

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0

    def deposit(self, amount):
        self.balance += amount
        m = Memento(self.balance)
        self.changes.append(Memento(self.balance))
        self.current += 1
        return m

    def restore(self, memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current += len(self.changes) - 1

    def undo(self):
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def redo(self):
        if self.current + 1 < len(self.changes):
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def __str__(self):
        return f"Balance = {self.balance}"


class Memento:
    def __init__(self, balance):
        self.balance = balance


if __name__ == "__main__":
    # ba = BankAccount(100)
    # # problem: we don't have the memento for the initial state
    # m1 = ba.deposit(50)
    # m2 = ba.deposit(25)
    # print(ba)
    # ba.restore(m1)
    # print(ba)
    # ba.restore(m2)
    # print(ba)

    ba = BankAccount(100)
    ba.deposit(50)
    ba.deposit(25)
    print(ba)

    ba.undo()
    ba.undo()
    print(ba)
    ba.redo()
    print(ba)
