class Bike:
    
    def __init__(self, make, model, year, category, capacity):
        self.make = make
        self.model = model
        self.year = year
        self.category = category
        self.odometer_reading = 0
        self.top_speed = 250
        self.service_length = 10000
        self.capacity = capacity

    def get_specs(self):
        print(f"Manufacturer: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Category: {self.category}")
        print(f"Odometer Reading: {self.odometer_reading} miles")
        
    
    def increment_odometer(self, miles):
        self.odometer_reading +=  miles
    
    def power_limiter(self, speed):
        self.top_speed -= speed
        print(f"Speed limited to {self.top_speed} kms")

    def service_interval(self):
        
        if self.capacity >= 1000:
            if self.odometer_reading >= self.service_length:
                print(f"{self.make} {self.model} is ready for servicing.")

            else:
                remaining_miles = self.service_length - self.odometer_reading
                print(f"{remaining_miles} miles remaining for your next service.")

        else:
            self.service_length //= 4

            if self.odometer_reading >= self.service_length:
                print(f"{self.make} {self.model} is ready for servicing.")

            else:
                remaining_miles = self.service_length - self.odometer_reading
                print(f"{remaining_miles} miles remaining for your next service.")

            


race_bike = Bike('Yamaha', 'MT 10', 2022, 'Naked', 1000)
race_bike.increment_odometer(2500)
race_bike.get_specs()
race_bike.power_limiter(100)
race_bike.service_interval()

print()

commute_bike = Bike('Suzuki', 'Access 125', 2020, 'Scooter', 125)
commute_bike.increment_odometer(1500)
commute_bike.get_specs()
commute_bike.service_interval()




