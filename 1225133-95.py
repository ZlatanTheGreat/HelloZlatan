import math

class Circle:
    def __init__(self, radius):
        Circle.radius = radius

    @classmethod
    def circumference(cls, radius):
        circumference = (2*radius) * math.pi
        print(f"Circumference = {round(circumference)}")

    @classmethod
    def area(cls, radius):
        area = math.pi * (radius**2)
        print(f'Area = {round(area)}')


Circle.circumference(10)
Circle.area(10)