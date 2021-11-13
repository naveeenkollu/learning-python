from bike import Bike


# Inheritance
class Electricbike(Bike):

    def __init__(self, make, model, year, category, capacity):
        # Inheriting from parent class 'Bike'
        super().__init__(make, model, year, category, capacity)


ev_scooter = Electricbike('Ather', '450X', 2020, 'Electric', 150)

print()
ev_scooter.get_specs()
ev_scooter.power_limiter(170)
ev_scooter.service_interval()


        