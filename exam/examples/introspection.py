class A:
    msg = "Simple text"

a = A()
# print(dir(a))
# print(type(1.2))
# print(type(a))
# print(type(type))
# print(type.__class__.__name__)
# print(type(int) == type)
# print(type(type) == type)
# print(type, type(int))
# print(type, type(a))
print(type == type(a))
print(type == type(A))
print(a.__class__.__class__)

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubclass(MyClass):
    pass