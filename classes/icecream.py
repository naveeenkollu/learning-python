from icecream import IceCreamStand

class IceCreamStand:

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = []

    def add_flavors(self, flavor):
            return self.flavors.append(flavor.title())

    def describe_flavors(self):
        print(f"Available flavors:")
        
        for flavor in self.flavors:
            print(f"- {flavor}")

icecream = IceCreamStand('Ibaco', 'Icecreams')
icecream.add_flavors('chocolate')
icecream.add_flavors('pista')
icecream.add_flavors('vanilla')
icecream.describe_flavors()
