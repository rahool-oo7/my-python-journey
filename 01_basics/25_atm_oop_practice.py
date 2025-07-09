# 25_atm_oop_practice.py
# ------------------------------------------------------------------------
# This script is a basic implementation of an ATM system using OOP concepts
# such as encapsulation and method definition to manage PIN and balance.

class ATM:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

    def create_pin(self, pin):
        self.__pin = pin
        print("PIN created successfully!")

    def deposit(self, pin, amount):
        if pin == self.__pin:
            self.__balance += amount
            print("Amount deposited.")
        else:
            print("Incorrect PIN.")

    def check_balance(self, pin):
        if pin == self.__pin:
            print(f"Balance: ₹{self.__balance}")
        else:
            print("Incorrect PIN.")

atm = ATM()
atm.create_pin("1234")
atm.deposit("1234", 500)
atm.check_balance("1234")
