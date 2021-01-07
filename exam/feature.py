class Point():
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(1, 2)
point2 = eval("Point(1, 2)")
point3 = getattr(sys.modules[__name__], "Point")(3, 6)
point4 = globals()["Point"](4, 8)
