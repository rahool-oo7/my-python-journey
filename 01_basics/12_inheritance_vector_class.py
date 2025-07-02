# 12_inheritance_vector_class.py
# -------------------------------------------------------------------
# This script demonstrates inheritance and method overriding.
# - vector2D class represents a 2D vector
# - vector3D inherits from vector2D and adds a third component

# Base class: 2D Vector
class vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i + {self.j}j")

# Derived class: 3D Vector (inherits from vector2D)
class vector3D(vector2D):
    def __init__(self, i, j, k):
        # Call base class constructor for i and j
        super().__init__(i, j)
        self.k = k

    # Override show method to include k component
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

# Create instances
a = vector2D(2, 3)
b = vector3D(2, 3, 4)

# Display vector components
print("2D Vector:")
a.show()

print("3D Vector:")
b.show()
