# 21_class_and_object_basics.py
# ------------------------------------------------------------------------
# This script demonstrates the basics of classes and objects in Python
# by creating a simple Student class with a method to display student details.
class Student:
    def __init__(self, name, roll):  # __init__ is the constructor.
        self.name = name             # self refers to the current instance.
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Creating an object
student1 = Student("Ritesh", 101)

# We create an object student1 using the Student class.

# Calling method
student1.display()
