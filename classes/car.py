class Car:

    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_tank = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name)

    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print('You can rollback  the odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_fuel_tank(self, count):
        self.fuel_tank += count
        print(f"Fuel up my car to {self.fuel_tank} litres")



# my_car = Car('porsche', '968', '1968')

# # Modifying the attribute value directly through the instance
# my_car.odometer_reading = 55
# my_car.get_descriptive_name()
# my_car.read_odometer()

# new_car = Car('porsche', '911GT3', 2021)
# new_car.get_descriptive_name()

# # Modifying the attribute value through a method
# new_car.update_odometer(99)
# new_car.read_odometer()
# new_car.fill_fuel_tank(25)


# my_car_1 = Car('porsche', '911 DLS Singer', 1970)
# my_car_1.get_descriptive_name()

# # Incrementing the attr. value through a method
# my_car_1.increment_odometer(15)
# my_car_1.read_odometer()

