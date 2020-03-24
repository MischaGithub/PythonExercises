#Declaring a super class called shapes
class Shapes:
    pass
#Importing math

import math

#Declaring the sub class of shapes and its functions
class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius
    def area(self,raduis):
        return math.pi*raduis**2
    def circumference(self):
        return 2 * math.pi * self.radius

#Prompting to enter the radius and also getting the output as per the method
rad = float(input("Enter radius of a circle: \n"))
objC = Circle(rad)
print("Area of a circle:", (objC.area(rad)))
print("Circumference of a cirle:",objC.circumference())






