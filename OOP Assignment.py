class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}, Year: {self.year}")
        
    def start_engine(self):
        print(f"The engine of {self.make} {self.model} is now running.")

class Bus(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Bus Capacity: {self.capacity} passengers")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Car Doors: {self.doors}")
        

car = Car("Toyota", "Corolla", 2020, 4)
bus = Bus("Mercedes", "Sprinter", 2019, 20)
car.display_info()
car.start_engine()
bus.display_info()
bus.start_engine()
print("End of OOP Assignment.")