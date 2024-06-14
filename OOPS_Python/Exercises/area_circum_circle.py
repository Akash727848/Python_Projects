from math import pi
class Circle:
    radius=9
    def __init__(self,radius):
        self.r=int(radius)
    def circumference(self):
        return f"The circumference of circle would be {2*pi*self.r}"
    def area(self):
        return f"The Area of circle would be {2*pi*(self.r**2)}"

def res():
    rvalue=input("Enter the value of Radius: " )
    result=Circle(rvalue)
    print(result.circumference())
    print(result.area())
res()