# 11_property_decorator_example.py
# ----------------------------------------------------------------
# This script demonstrates use of @property and @setter in a class.
# It allows setting and getting full name as a property.

class Employee:

    # Getter method for the 'name' property
    @property
    def name(self):
        return f"The name is {self.fname} {self.lname}"

    # Setter method for the 'name' property
    @name.setter
    def name(self, fullname):
        # Automatically splits fullname into first and last name
        self.ename = fullname
        self.fname = fullname.split(" ")[0]
        self.lname = fullname.split(" ")[1]

# Create an Employee instance
e = Employee()

# Set full name (calls the setter)
e.name = "Ritesh Kumar"

# Get full name (calls the getter)
print(e.name)

# Access individual attributes
print("First name:", e.fname)
print("Last name :", e.lname)
