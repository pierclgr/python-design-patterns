import unittest

from command import *

class CompositeBankAccountCommand(Command, list):
    # and implementation of the composite design pattern for commands
    def __init__(self, items=None):
        if not items:
            items = []

        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for cmd in self:
            cmd.invoke()

    def undo(self):
        for cmd in reversed(self):
            cmd.undo()

class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_account, to_account, amount):
        super().__init__([
            BankAccountCommand(from_account, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_account, BankAccountCommand.Action.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False

        self.success = ok

class TestSuite(unittest.TestCase):
    # def test_composite_deposit(self):
    #     ba = BankAccount()
    #     deposit1 = BankAccountCommand(
    #         ba, BankAccountCommand.Action.DEPOSIT, 100
    #     )
    #     deposit2 = BankAccountCommand(
    #         ba, BankAccountCommand.Action.DEPOSIT, 50
    #     )
    #
    #     composite = CompositeBankAccountCommand([deposit1, deposit2])
    #     composite.invoke()
    #     composite.undo()

    # def test_transfer_fail(self):
    #     ba1 = BankAccount(100)
    #     ba2 = BankAccount()
    #
    #     amount = 1000
    #     wd = BankAccountCommand(
    #         ba1, BankAccountCommand.Action.WITHDRAW, amount
    #     )
    #
    #     # this command should depend on the success of the previous command
    #     dp = BankAccountCommand(
    #         ba2, BankAccountCommand.Action.DEPOSIT, amount
    #     )
    #
    #     transfer = CompositeBankAccountCommand([wd, dp])
    #     transfer.invoke()
    #     print(f"ba1: {ba1}, ba2: {ba2}")
    #     transfer.undo()
    #     print(f"ba1: {ba1}, ba2: {ba2}")

    # def test_better_transfer(self):
    #     ba1 = BankAccount(100)
    #     ba2 = BankAccount()
    #     print(f"ba1: {ba1}, ba2: {ba2}")
    #
    #     amount = 100
    #     transfer = MoneyTransferCommand(ba1, ba2, amount)
    #     transfer.invoke()
    #     print(f"ba1: {ba1}, ba2: {ba2}")
    #     transfer.undo()
    #     print(f"ba1: {ba1}, ba2: {ba2}")
    #     print(transfer.success)

    def test_better_transfer_failed(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()
        print(f"ba1: {ba1}, ba2: {ba2}")

        amount = 1000
        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print(f"ba1: {ba1}, ba2: {ba2}")
        transfer.undo()
        print(f"ba1: {ba1}, ba2: {ba2}")
        print(transfer.success)

if __name__ == "__main__":
    unittest.main()

