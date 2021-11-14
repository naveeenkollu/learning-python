from abc import ABC, abstractmethod

# Inherited abc class
class UIControl(ABC):
    
    @abstractmethod
    def draw(self):
        pass

# Inherited UIControl
class TextBox(UIControl):
    
    def draw(self):
        print('TextBox')

# Inherited UIControl
class DropDownList(UIControl):
    
    def draw(self):
        print('DropDownList')


# draw() defined here is not bound to any class
# paramaters we are passing for draw() is an instance of an object which calls the draw() method in that function 
def draw(controls):
    controls.draw()


ddl = DropDownList()
print(draw(ddl))

tb = TextBox()
print(draw(tb))