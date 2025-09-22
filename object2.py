# Base class Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def check_battery(self):
        print(f"Battery life remaining: {self.battery_life} hours")

# Subclass GamingSmartphone inherits Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system  # e.g. "Liquid cooling"

    # Override check_battery to add gaming mode info
    def check_battery(self):
        print(f"Battery life (Gaming Mode): {self.battery_life - 2} hours")
        print(f"Cooling system active: {self.cooling_system}")

# Example usage
phone = Smartphone("Apple", "iPhone 15", 20)
phone.make_call("123-456-7890")
phone.check_battery()

g_phone = GamingSmartphone("ASUS", "ROG Phone 7", 10, "Liquid Cooling")
g_phone.make_call("987-654-3210")
g_phone.check_battery()
#Multiple Inheritance

class Animal:
    def move(self):
        print("This animal moves")

class Dog(Animal):
    def move(self):
        print("Dog runs")

class Fish(Animal):
    def move(self):
        print("Fish swims")

class Bird(Animal):
    def move(self):
        print("Bird flies")

# List of animals demonstrating polymorphism
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()
