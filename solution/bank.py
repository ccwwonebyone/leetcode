from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.total = len(self.balance) - 1

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account2 -= 1
        account1 -= 1
        if account2 > self.total or account1 > self.total:
            return False
        if self.balance[account1] > money:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if account > self.total:
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if account > self.total:
            return False

        if self.balance[account] >= money:
            self.balance[account] -= money
            return True
        return False
