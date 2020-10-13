class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_Area(self):
        return self.a * self.b
class Square:
    def __init__(self, a):
        self.a = a
    def get_Area_Square(self):
        return self.a ** 2
class Circle:
    def __init__(self, r):
        self.a = r
    def get_Circle_Square(self):
        import math
        return round(math.pi *self.a ** 2 / 2, 2)