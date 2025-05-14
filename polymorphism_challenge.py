class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create a list of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Polymorphic behavior
for v in vehicles:
    v.move()
