# from module import class
# Here Python is saying to open the module named 'car' & import class named 'Car'
from car import Car

new_car = Car('kia', 'seltos', 2020)
new_car.get_descriptive_name()
new_car.read_odometer()
new_car.update_odometer(50)
new_car.read_odometer()