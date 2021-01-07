import weakref
import gc

class A:
    def some(self):
        print("Кирил пидорас")

a = A()
proxy_a = weakref.proxy(a)
ref_a = weakref.ref(a)
print(proxy_a)
print(ref_a)
del A
del a
gc.collect()
# print(proxy_a) ReferenceError: weakly-referenced object no longer exists
print(ref_a)