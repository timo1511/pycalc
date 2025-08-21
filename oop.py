"""
This script combines the assignment for OOP:
1. Created a superhero class that demonstrates inheritance as well as encapsulation.
2. Provides a polymorphism challenge demonstrated using various vehicle types.
"""

# --- Assignment 1: Design Own Class in Python ---
print("--- Assignment 1: Superhero Class ---")

class Human:
    """A simple parent class representing a human."""
    def __init__(self, name):
        self.name = name
        self.species = "Homo sapiens"

    def speak(self):
        return f"Hello, my name is {self.name}."

class Superhero(Human):
    """
    Represents a Superhero.
    Inherits from the Human class and adds unique attributes and methods.
    """
    def __init__(self, name, hero_name, power, strength_level):
        # Initialize the parent Human class with the real name
        super().__init__(name)
        
        # Superhero-specific attributes
        self.hero_name = hero_name
        self.power = power
        self.strength_level = strength_level
        
        # Encapsulation: This attribute is intended for internal use
        # The single underscore is a convention to indicate it's "protected".
        self._secret_identity_known = False

    def use_power(self):
        """A method for the superhero to use their power."""
        return f"{self.hero_name} uses their power of {self.power}!"

    def introduce(self):
        """
        Overrides the parent's speak method to provide a heroic introduction.
        This is a form of polymorphism.
        """
        return f"Fear not! I am {self.hero_name}!"
        
    def reveal_secret_identity(self):
        """A method to control access to the 'protected' attribute."""
        self._secret_identity_known = True
        # We access the 'name' attribute inherited from the Human class
        return f"My secret identity is {self.name}. The world knows now!"

# --- Creating instances (objects) of the Superhero class ---
# Initialize each object with unique values
superman = Superhero("Clark Kent", "Superman", "Flight and Super Strength", 100)
spider_man = Superhero("Peter Parker", "Spider-Man", "Wall-crawling and Spider-sense", 75)

# --- Using the methods ---
print(superman.introduce())
print(spider_man.introduce())

print(superman.use_power())
print(f"Superman's strength level is: {superman.strength_level}")

# The 'speak' method is inherited from the Human class
print(f"When not in costume, he says: '{spider_man.speak()}'")

# Accessing the encapsulated data via a controlled method
print(superman.reveal_secret_identity())


print("\n" + "="*40 + "\n")


# --- Activity 2: Polymorphism Challenge! 🎭 ---
print("--- Activity 2: Polymorphism Challenge ---")

class Car:
    """A class representing a Car."""
    def __init__(self, model):
        self.model = model
    
    def move(self):
        """Defines how a car moves."""
        print(f"The {self.model} is Driving 🚗")

class Plane:
    """A class representing a Plane."""
    def __init__(self, model):
        self.model = model

    def move(self):
        """Defines how a plane moves."""
        print(f"The {self.model} is Flying ✈️")

class Boat:
    """A class representing a Boat."""
    def __init__(self, model):
        self.model = model

    def move(self):
        """Defines how a boat moves."""
        print(f"The {self.model} is Sailing ⛵")


# --- Creating instances of the vehicle classes ---
car1 = Car("Toyota Camry")
plane1 = Plane("Boeing 747")
boat1 = Boat("Sailboat")

# --- Demonstrating Polymorphism ---
# We can treat each object the same way (call .move())
# but get different, class-specific results.
vehicles = [car1, plane1, boat1]

for vehicle in vehicles:
    # Python doesn't care what class 'vehicle' is.
    # It only cares that it has a .move() method.
    vehicle.move()

