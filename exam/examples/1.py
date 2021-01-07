from functools import partial
from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "norm"])

def norm(point):
    return point.x + point.y

Point = partial(Point, norm=norm)
p1 = Point(1, 2)
print(p1)
print(p1.__class__)
# print(Point.norm(p1)) Вот так не можем делать
print(p1.norm(p1))