class Pizza:
    def __init__(self, radius):
        # Private Variables
        self._radius = radius

    # To access the value of the variable outside class
    @property
    def radius(self):
        return self._radius

    # To change the value of a class variable reliably
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Pizza size must be positive!")
    
    @property
    def diameter(self):
        return self._radius * 2
    
    # To delete
    @radius.deleter
    def radius(self):
        print("Values Cleaned")
        del self._radius

class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

class Person:
    species = "Homo Erectus"

    @classmethod
    def get_species(cls):
        print(cls)
        return cls.species

# Usage
p = Pizza(12)
print(p.radius)
print(p.diameter)
p.radius = 8
print(p.radius)
print(p.diameter)

# delete instance
del p.radius

# Can be directly called without creating an instance
print(Math.add(3,4))
print(Math.multiply(2,4))

##
print(Person.get_species())