class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount to deposit should be greater than zero.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount to withdraw should be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
