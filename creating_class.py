# Base class
class Laptop:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self._battery_life = battery_life  # Encapsulated attribute

    def specs(self):
        return f"Laptop Specs:\nBrand: {self.brand}\nModel: {self.model}\nPrice: ${self.price}\nBattery Life: {self._battery_life} hours"

    def is_affordable(self):
        return self.price < 1000

    def get_battery_life(self):  # Encapsulation getter
        return self._battery_life

    def set_battery_life(self, hours):  # Encapsulation setter
        if hours > 0:
            self._battery_life = hours
        else:
            print("Battery life must be positive.")

# Subclass
class GamingLaptop(Laptop):
    def __init__(self, brand, model, price, battery_life, gpu, cooling_system):
        super().__init__(brand, model, price, battery_life)
        self.gpu = gpu
        self.cooling_system = cooling_system

    # Override the specs method (polymorphism)
    def specs(self):
        base_specs = super().specs()
        return f"{base_specs}\nGPU: {self.gpu}\nCooling: {self.cooling_system}"

# Example usage
l1 = Laptop("Dell", "XPS 13", 999, 12)
g1 = GamingLaptop("Asus", "ROG Zephyrus", 1800, 6, "NVIDIA RTX 4070", "Advanced Vapor Chamber")

print(l1.specs())
print("\nAffordable?", l1.is_affordable())

print("\n" + "-"*40 + "\n")

print(g1.specs())
print("\nAffordable?", g1.is_affordable())
