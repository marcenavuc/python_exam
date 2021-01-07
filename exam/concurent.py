from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep


def a(mes, text: str):
    print("I'm sleeping")
    sleep(2)
    print(text)
    return mes


pool = ThreadPoolExecutor(5)
# future = pool.submit(a, "Hi")
# print(future.done())
# sleep(5)
# print(future.done())
# print(future.result())
results = pool.map(a, [(1, "Hi"), (2, "yaya")])
print(results)
for future in results:
    print(future)
    # print(future.result())
