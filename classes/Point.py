class Point:

    # Constructor function of class 'Point'
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Class method 
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # magic methods - special methods already available in Python
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Member functions of class 'Point'/ instance method of any defined object
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Creating a new object instance of 'Point'
point = Point(1, 2)
print(point)

# Calling the 'point' object and invoking the method 'draw()' using dot notation  
point.draw()

# Calling the class method and setting it to object instance 'point'
point = Point.zero()
point.draw()




