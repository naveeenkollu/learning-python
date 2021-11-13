from car import Car
from battery import Battery


class Electriccar:

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
        self.battery = Battery()

    def fill_fuel_tank(self):
        print("Electric cars don't have fuel tanks.")


ev_car = Electriccar('porsche', 'Taycan', 2020)
ev_car.get_descriptive_name()

# Instances as Attributes
ev_car.battery.describe_battery()    
ev_car.battery.upgrade_battery()






