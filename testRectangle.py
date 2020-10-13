from rectangle import Rectangle, Square, Circle
r1 = Rectangle(3, 4)
r2 = Rectangle(12, 5)

sq1 = Square(5)
sq2 = Square(10)

c1 = Circle(5)
c2 = Circle(7)

figures = [r1, r2, sq1, sq2, c1, c2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_Area_Square())
    elif isinstance(figure, Circle):
        print(figure.get_Circle_Square())
    else:
        print(figure.get_Area())