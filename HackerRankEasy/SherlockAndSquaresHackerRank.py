
from math import sqrt,ceil,floor

def squares(a,b):
    count=0
    for i in range(a,b+1):
        if sqrt(i)%int(sqrt(i))==0:
            count+=1
    return count

def squares2(a,b):
    count=0
    sqrta=sqrt(a)
    sqrtb=sqrt(b)
    ceila=ceil(sqrta)
    floorb=floor(sqrtb)
    count=floorb-ceila+1
    return count

if __name__=="__main__":
    q=int(input("Enter the number of test cases: "))
    for i in range(q):
        a=int(input("Enter the value of a: "))
        b=int(input("Enter the value of b: "))
        print(squares2(a,b))







