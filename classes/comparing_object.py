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

    # magic method for comparing two objects 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # magic method for comparing which is greater of two objects 
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
        
    # magic method for comparing which is lesser of two objects 
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
        
    # Member functions of class 'Point'/ instance method of any defined object
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
other = Point(1, 2)

print(point == other)
print(point > other)
print(point < other)