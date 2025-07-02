# 13_inheritance_and_employee_class.py
# ------------------------------------------------------------------
# Part 1: Demonstrates multilevel inheritance
# Part 2: Shows the difference between class-level and instance-level attributes

# ---------------- MULTILEVEL INHERITANCE ----------------
class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    def bark(self, sound):
        print(f"Dog sound: {sound}")

# Create Dog object and call bark method
d = Dog()
d.bark("Bhow Bhow")

# ---------------- EMPLOYEE CLASS ----------------
# Version 1: Class-level attributes (shared by all instances)
class EmployeeClassLevel:
    name = "Ritesh Kumar"
    salary = 1000000
    company = "Microsoft"

# Version 2: Instance-level attributes (unique per object)
class EmployeeInstanceLevel:
    def __init__(self):
        self.name = "Ritesh Kumar"
        self.salary = 1000000
        self.company = "Microsoft"

# Create objects for both types
emp1 = EmployeeClassLevel()
emp2 = EmployeeInstanceLevel()

# Print attributes
print("\n--- Class Level Employee ---")
print(emp1.name, emp1.salary, emp1.company)

print("\n--- Instance Level Employee ---")
print(emp2.name, emp2.salary, emp2.company)
