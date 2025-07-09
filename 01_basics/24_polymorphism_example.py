# 24_polymorphism_example.py
# ------------------------------------------------------------------------
# This script demonstrates polymorphism in Python by using
# the same method name in different classes with different behavior.

class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

for bird in [Bird(), Penguin()]:
    bird.fly()
