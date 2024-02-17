class Car:
    # Class attribute
    wheels = 4

    # Constructor method (initializer)
    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    # Instance method
    def start(self):
        if not self.is_running:
            print(f"Starting the {self.year} {self.make} {self.model}.")
            self.is_running = True
        else:
            print("The car is already running.")

    # Instance method
    def stop(self):
        if self.is_running:
            print(f"Stopping the {self.year} {self.make} {self.model}.")
            self.is_running = False
        else:
            print("The car is already stopped.")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model S", 2023)

# Accessing class attributes
print(f"A car typically has {Car.wheels} wheels.")

# Accessing instance attributes
print(f"The first car is a {car1.year} {car1.make} {car1.model}.")
print(f"The second car is a {car2.year} {car2.make} {car2.model}.")

# Calling instance methods
car1.start()
car2.start()
car1.stop()
car2.stop()