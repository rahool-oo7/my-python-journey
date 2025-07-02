# 10_class_and_objects_basics.py
# ----------------------------------------------------------------
# This script demonstrates the basics of classes and objects in Python:
# - Class variables
# - Instance variables
# - Constructor (__init__)
# - Object creation and access

# ---------- EMPLOYEE CLASS ----------
class Employee:
    language = "Python"       # Class variable
    salary = 1000000          # Class variable

    def __init__(self, name):
        self.name = name      # Instance variable

# Taking name input and creating object
name = input("Enter your name: ")
obj1 = Employee(name)

# Access class and instance variables
print(obj1.language, obj1.salary, obj1.name)


# ---------- PROGRAMMERS CLASS ----------
class Programmers:
    company = "Microsoft"     # Class variable

    def __init__(self, name, language, salary):
        self.name = name          # Instance variable
        self.language = language
        self.salary = salary

# Creating multiple Programmer objects
ritesh = Programmers("Ritesh", "Python", 1200000)
rohan = Programmers("Rohan", "Python", 1200000)
mohit = Programmers("Mohit", "Python", 1200000)

# Accessing data from the object 'ritesh'
print("\n--- Programmer Details ---")
print("Name     :", ritesh.name)
print("Language :", ritesh.language)
print("Salary   :", ritesh.salary)
print("Company  :", ritesh.company)
