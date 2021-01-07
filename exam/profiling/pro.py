import cProfile
import hashlib
import time

def fast():
    print("Я быстрая функция")
 
 
def slow():
    time.sleep(3)
    print("Я очень медленная функция")
 
 
def medium():
    time.sleep(0.5)
    print("Я средняя функция...")
 
 
def main():
    fast()
    slow()
    medium()
 
if __name__ == '__main__':
    # cProfile.run("main()")
    main()
