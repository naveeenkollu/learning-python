class Point:

    # Constructor function of class 'Point'
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # Member functions of class 'Point'
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Creating a new object instance of 'Point'
point = Point(1, 2)

# Calling the 'point' object and invoking the method 'draw()' using dot notation  
point.draw()
