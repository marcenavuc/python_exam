
def real(x, y):
    num_days = 1
    while x < y:
        x *= 1.1
        num_days += 1

    print(num_days)

def solution(x, y):
    X=x
    Y=y
    X += (Y/100*10)
    print(X) 
    
real(10, 30)
solution(10, 30)
real(10, 20)
solution(10, 20)