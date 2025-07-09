# 23_inheritance_and_method_override.py
# ------------------------------------------------------------------------
# This script demonstrates inheritance and method overriding
# with a base Animal class and a derived Dog class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
a.speak()

d = Dog()
d.speak()
