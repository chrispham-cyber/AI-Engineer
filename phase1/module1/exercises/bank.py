"""class Account:
    def __init__(self, user, balance=0):
        self.user = user
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Invalid withdrawal amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, target_account):
        if amount < 0:
            raise ValueError("Invalid transfer amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer")
        self.withdraw(amount)
        target_account.deposit(amount)"""

from dataclasses import dataclass

@dataclass
class Account:
    user: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Invalid withdrawal amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, target_account):
        if amount < 0:
            raise ValueError("Invalid transfer amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer")
        self.withdraw(amount)
        target_account.deposit(amount)

ba1 = Account("Alice", 1000)
ba2 = Account("Bob", 500)

print(f"Alice's balance: {ba1.get_balance()}")

ba1.deposit(2000)

print(f"Alice's balance after deposit: {ba1.get_balance()}")

ba1.withdraw(500)

print(f"Alice's balance after withdrawal: {ba1.get_balance()}")

ba1.transfer(300, ba2)
print(f"Alice's balance after transfer: {ba1.get_balance()}")
print(f"Bob's balance after transfer: {ba2.get_balance()}")