# import math

# def PrimeOrNot(a):
#     if math.sqrt(a).is_integer():
#         return "Not a prime"
#     else:
#         li=[2,3,5,7]
#         if not a in li:
#             for i in li:
#                 if a%i==0:
#                     return "Not a prime"
#         if a>10:
#             for i in range(2,int(a/2+1)):
#                 if a%i==0:
#                     return "Not a prime"
#     return "Prime"
    
# numOfValues=int(input())
# data=[]
# for i in range(numOfValues):
#     number=int(input())
#     data.append(number)
# for i in data:
#     print(PrimeOrNot(i))


def PrimeOrNot(a):
    if a<=1:
        return False
    if a<=3:
        return True
    
    if a%2==0 or a%3==0:
        return False
    i=5

    while(i*i<=a):
        if (a%i==0 or a%(i+2)==0):
            return False
        i=i+6
    return True

numOfValues=int(input())
data=[]
for i in range(numOfValues):
    number=int(input())
    data.append(number)
for i in data:
    if (PrimeOrNot(i)):
        print("Prime")
    else:
        print("Not prime")