class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display(self):
        print("Model:", self.model)
        print("Year:", self.year)

    def service(self):
        print("Service for Vehicle")


class Car(Vehicle):
    def __init__(self, model, year, doors):
        super().__init__(model, year)
        self.doors = doors

    def display(self):
        super().display()
        print("Doors:", self.doors)

    def service(self):
        print("Car service includes oil change, brake check, and tire rotation.")


class Bike(Vehicle):
    def __init__(self, model, year, abs):
        super().__init__(model, year)
        self.abs = abs

    def display(self):
        super().display()
        print("ABS:", "Yes" if self.abs else "No")

    def service(self):
        print("Bike service includes chain lubrication, brake adjustment, and air check.")


# Main Program
print("-------- Vehicle Service Center --------")
print("1. Car")
print("2. Bike")

choice = int(input("Enter your choice: "))

if choice == 1:
    model = input("Enter Car Model: ")
    year = int(input("Enter Year: "))
    doors = int(input("Enter Number of Doors: "))

    v = Car(model, year, doors)
    print("\n--- Vehicle Details ---")
    v.display()
    print("--- Service Procedure ---")
    v.service()

elif choice == 2:
    model = input("Enter Bike Model: ")
    year = int(input("Enter Year: "))
    abs = input("Has ABS (true/false): ").lower() == "true"

    b = Bike(model, year, abs)
    print("\n--- Vehicle Details ---")
    b.display()
    print("--- Service Procedure ---")
    b.service()

else:
    print("Invalid Choice!")
