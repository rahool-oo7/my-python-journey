# 22_encapsulation_private_variable.py
# ------------------------------------------------------------------------
# This script demonstrates encapsulation by defining a BankAccount class
# with private variables and controlled access using methods.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
