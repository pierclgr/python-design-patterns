# Command Pattern
# The command pattern is a pattern that is used to create an object representing an instruction to perform a particular
# action. The object will contain all information necessary for this action to be taken.
from abc import ABC
from enum import Enum

class BankAccount:
    OVERDRAFT_LIMIT = 0

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, "
              f"balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, "
                  f"balance = {self.balance}")
            return True
        else:
            print(f"Balance is too low: {self.balance}")
            return False

    def __str__(self):
        return f"Balance = {self.balance}"

class Command(ABC):
    def __init__(self):
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass

class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)

if __name__ == "__main__":
    ba = BankAccount()
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.DEPOSIT, 100
    )
    cmd.invoke()
    cmd.undo()

    illegal_command = BankAccountCommand(
        ba, BankAccountCommand.Action.WITHDRAW, 1000
    )
    illegal_command.invoke()
    illegal_command.undo()
    print(ba)