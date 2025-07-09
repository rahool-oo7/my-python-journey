# 26_multiple_inheritance_example.py
# ------------------------------------------------------------------------
# This script demonstrates multiple inheritance in Python,
# where a child class inherits from two parent classes and combines their functionality.

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

class Student:
    def __init__(self, roll_no):
        self.roll_no = roll_no

    def show_roll(self):
        print(f"Roll No: {self.roll_no}")

class CollegeStudent(Person, Student):
    def __init__(self, name, roll_no, college):
        Person.__init__(self, name)
        Student.__init__(self, roll_no)
        self.college = college

    def show_details(self):
        self.show_name()
        self.show_roll()
        print(f"College: {self.college}")

# Create object of CollegeStudent
student = CollegeStudent("Ritesh", 101, "Presidency University")
student.show_details()
