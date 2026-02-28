# Data hiding organize data to prevent data access by any function that is not specified in class.
# In python member are public by default.
"""
Demonstrates encapsulation using private variables
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rahul", 1000)

account.deposit(500)
account.withdraw(300)

print("Current Balance:", account.get_balance())