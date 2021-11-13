class Battery:

    def __init__(self):
        self.battery_size = 0

    def describe_battery(self):
        print(f"This car has {self.battery_size}-kWH battery.")

    def upgrade_battery(self):
        if self.battery_size == 0:
            self.battery_size += 100
            print(f"The battery is updated to {self.battery_size}-kWH battery.")

        else:
            self.battery_size
